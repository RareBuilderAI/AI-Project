from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DATABASE = "links.db"


def get_database():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_database():
    connection = get_database()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS profile (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            bio TEXT NOT NULL
        )
        """
    )

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL
        )
        """
    )

    existing_profile = connection.execute(
        """
        SELECT id
        FROM profile
        WHERE id = 1
        """
    ).fetchone()

    if existing_profile is None:
        connection.execute(
            """
            INSERT INTO profile (
                id,
                name,
                bio
            )
            VALUES (?, ?, ?)
            """,
            (
                1,
                "Raremotion Labs",
                "AI • Automation • Code • Creative Tech"
            )
        )

    connection.commit()
    connection.close()


@app.route("/")
def home():
    connection = get_database()

    profile = connection.execute(
        """
        SELECT *
        FROM profile
        WHERE id = 1
        """
    ).fetchone()

    links = connection.execute(
        """
        SELECT *
        FROM links
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        profile=profile,
        links=links
    )


@app.route("/add-link", methods=["POST"])
def add_link():
    title = request.form.get("title", "").strip()
    url = request.form.get("url", "").strip()

    if title and url:

        if not url.startswith(
            (
                "http://",
                "https://"
            )
        ):
            url = "https://" + url

        connection = get_database()

        connection.execute(
            """
            INSERT INTO links (
                title,
                url
            )
            VALUES (?, ?)
            """,
            (
                title,
                url
            )
        )

        connection.commit()
        connection.close()

    return redirect(
        url_for("home")
    )


@app.route("/delete-link/<int:link_id>", methods=["POST"])
def delete_link(link_id):
    connection = get_database()

    connection.execute(
        """
        DELETE FROM links
        WHERE id = ?
        """,
        (link_id,)
    )

    connection.commit()
    connection.close()

    return redirect(
        url_for("home")
    )


@app.route("/update-profile", methods=["POST"])
def update_profile():
    name = request.form.get(
        "name",
        ""
    ).strip()

    bio = request.form.get(
        "bio",
        ""
    ).strip()

    if name and bio:

        connection = get_database()

        connection.execute(
            """
            UPDATE profile
            SET
                name = ?,
                bio = ?
            WHERE id = 1
            """,
            (
                name,
                bio
            )
        )

        connection.commit()
        connection.close()

    return redirect(
        url_for("home")
    )


if __name__ == "__main__":
    create_database()

    app.run(
        debug=True
    )