from flask import Flask, render_template, request, redirect
import sqlite3
import random
import string

app = Flask(__name__)

DATABASE = "urls.db"


def get_database():
    return sqlite3.connect(DATABASE)


def create_database():
    connection = get_database()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT NOT NULL UNIQUE,
            clicks INTEGER DEFAULT 0
        )
        """
    )

    connection.commit()
    connection.close()


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    return "".join(
        random.choice(characters)
        for _ in range(length)
    )


@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None
    error = None

    if request.method == "POST":
        original_url = request.form.get("url", "").strip()

        if not original_url:
            error = "Please enter a URL."

        else:
            if not original_url.startswith(("http://", "https://")):
                original_url = "https://" + original_url

            connection = get_database()

            while True:
                short_code = generate_short_code()

                existing = connection.execute(
                    """
                    SELECT id
                    FROM urls
                    WHERE short_code = ?
                    """,
                    (short_code,)
                ).fetchone()

                if existing is None:
                    break

            connection.execute(
                """
                INSERT INTO urls (
                    original_url,
                    short_code
                )
                VALUES (?, ?)
                """,
                (original_url, short_code)
            )

            connection.commit()
            connection.close()

            short_url = request.host_url + short_code

    return render_template(
        "index.html",
        short_url=short_url,
        error=error
    )


@app.route("/<short_code>")
def open_short_url(short_code):
    connection = get_database()

    result = connection.execute(
        """
        SELECT original_url
        FROM urls
        WHERE short_code = ?
        """,
        (short_code,)
    ).fetchone()

    if result is None:
        connection.close()
        return "Short URL not found.", 404

    connection.execute(
        """
        UPDATE urls
        SET clicks = clicks + 1
        WHERE short_code = ?
        """,
        (short_code,)
    )

    connection.commit()
    connection.close()

    return redirect(result[0])


if __name__ == "__main__":
    create_database()
    app.run(debug=True)