from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = "portfolio.db"


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
            title TEXT NOT NULL,
            bio TEXT NOT NULL
        )
        """
    )

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            project_url TEXT,
            github_url TEXT,
            tech_stack TEXT
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
                title,
                bio
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                1,
                "Raremotion Labs",
                "AI Software & Automation Studio",
                "Building AI tools, automation systems, software projects and useful digital products."
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

    projects = connection.execute(
        """
        SELECT *
        FROM projects
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        profile=profile,
        projects=projects
    )


@app.route("/add-project", methods=["POST"])
def add_project():
    title = request.form.get(
        "title",
        ""
    ).strip()

    description = request.form.get(
        "description",
        ""
    ).strip()

    project_url = request.form.get(
        "project_url",
        ""
    ).strip()

    github_url = request.form.get(
        "github_url",
        ""
    ).strip()

    tech_stack = request.form.get(
        "tech_stack",
        ""
    ).strip()

    if title and description:

        if project_url and not project_url.startswith(
            ("http://", "https://")
        ):
            project_url = "https://" + project_url

        if github_url and not github_url.startswith(
            ("http://", "https://")
        ):
            github_url = "https://" + github_url

        connection = get_database()

        connection.execute(
            """
            INSERT INTO projects (
                title,
                description,
                project_url,
                github_url,
                tech_stack
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                title,
                description,
                project_url,
                github_url,
                tech_stack
            )
        )

        connection.commit()
        connection.close()

    return redirect(
        url_for("home")
    )


@app.route(
    "/update-project/<int:project_id>",
    methods=["POST"]
)
def update_project(project_id):
    title = request.form.get(
        "title",
        ""
    ).strip()

    description = request.form.get(
        "description",
        ""
    ).strip()

    project_url = request.form.get(
        "project_url",
        ""
    ).strip()

    github_url = request.form.get(
        "github_url",
        ""
    ).strip()

    tech_stack = request.form.get(
        "tech_stack",
        ""
    ).strip()

    if project_url and not project_url.startswith(
        ("http://", "https://")
    ):
        project_url = "https://" + project_url

    if github_url and not github_url.startswith(
        ("http://", "https://")
    ):
        github_url = "https://" + github_url

    if title and description:
        connection = get_database()

        connection.execute(
            """
            UPDATE projects
            SET
                title = ?,
                description = ?,
                project_url = ?,
                github_url = ?,
                tech_stack = ?
            WHERE id = ?
            """,
            (
                title,
                description,
                project_url,
                github_url,
                tech_stack,
                project_id
            )
        )

        connection.commit()
        connection.close()

    return redirect(
        url_for("home")
    )


@app.route(
    "/delete-project/<int:project_id>",
    methods=["POST"]
)
def delete_project(project_id):
    connection = get_database()

    connection.execute(
        """
        DELETE FROM projects
        WHERE id = ?
        """,
        (project_id,)
    )

    connection.commit()
    connection.close()

    return redirect(
        url_for("home")
    )


@app.route(
    "/update-profile",
    methods=["POST"]
)
def update_profile():
    name = request.form.get(
        "name",
        ""
    ).strip()

    title = request.form.get(
        "title",
        ""
    ).strip()

    bio = request.form.get(
        "bio",
        ""
    ).strip()

    if name and title and bio:
        connection = get_database()

        connection.execute(
            """
            UPDATE profile
            SET
                name = ?,
                title = ?,
                bio = ?
            WHERE id = 1
            """,
            (
                name,
                title,
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