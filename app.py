import os
import sqlite3

from datetime import datetime

from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    send_from_directory
)

from tool_router import ToolRouter

app = Flask(__name__)

DATABASE = "finance.db"

tool_router = ToolRouter()

# =========================================
# DATABASE
# =========================================

def get_connection():

    connection = sqlite3.connect(
        DATABASE
    )

    connection.row_factory = sqlite3.Row

    return connection


def init_db():

    connection = get_connection()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS income (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
        """
    )

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
        """
    )

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS budget (
            id INTEGER PRIMARY KEY,
            amount REAL NOT NULL
        )
        """
    )

    connection.commit()

    connection.close()


init_db()


# =========================================
# ROBOTCHAT DASHBOARD
# =========================================

@app.route("/")
def home():

    connection = get_connection()

    income = connection.execute(
        "SELECT * FROM income ORDER BY id DESC"
    ).fetchall()

    expenses = connection.execute(
        "SELECT * FROM expenses ORDER BY id DESC"
    ).fetchall()

    budget_row = connection.execute(
        "SELECT amount FROM budget WHERE id = 1"
    ).fetchone()

    connection.close()

    total_income = sum(
        entry["amount"]
        for entry in income
    )

    total_expenses = sum(
        expense["amount"]
        for expense in expenses
    )

    balance = total_income - total_expenses

    budget = (
        budget_row["amount"]
        if budget_row
        else 0
    )

    current_month = datetime.now().strftime(
        "%Y-%m"
    )

    monthly_expenses_total = sum(
        expense["amount"]
        for expense in expenses
        if expense["date"].startswith(
            current_month
        )
    )

    budget_remaining = (
        budget - monthly_expenses_total
    )

    return render_template(
        "index.html",
        income=income,
        expenses=expenses,
        total_income=total_income,
        total_expenses=total_expenses,
        balance=balance,
        budget=budget,
        budget_remaining=budget_remaining
    )


# =========================================
# ADD INCOME
# =========================================

@app.route(
    "/add-income",
    methods=["POST"]
)
def add_income():

    data = request.get_json(
        silent=True
    ) or {}

    name = data.get(
        "name",
        ""
    ).strip()

    amount_text = data.get(
        "amount",
        ""
    ).strip()

    if not name:

        return jsonify({
            "error": "Income name is required."
        }), 400

    if not amount_text:

        return jsonify({
            "error": "Income amount is required."
        }), 400

    try:

        amount = float(
            amount_text
        )

    except ValueError:

        return jsonify({
            "error": "Please enter a valid amount."
        }), 400

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO income (
            name,
            amount,
            date
        )
        VALUES (?, ?, ?)
        """,
        (
            name,
            amount,
            datetime.now().strftime(
                "%Y-%m-%d"
            )
        )
    )

    connection.commit()

    connection.close()

    return jsonify({
        "message": "Income added successfully."
    })


# =========================================
# ADD EXPENSE
# =========================================

@app.route(
    "/add-expense",
    methods=["POST"]
)
def add_expense():

    data = request.get_json(
        silent=True
    ) or {}

    name = data.get(
        "name",
        ""
    ).strip()

    amount_text = data.get(
        "amount",
        ""
    ).strip()

    if not name:

        return jsonify({
            "error": "Expense name is required."
        }), 400

    if not amount_text:

        return jsonify({
            "error": "Expense amount is required."
        }), 400

    try:

        amount = float(
            amount_text
        )

    except ValueError:

        return jsonify({
            "error": "Please enter a valid amount."
        }), 400

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO expenses (
            name,
            amount,
            date
        )
        VALUES (?, ?, ?)
        """,
        (
            name,
            amount,
            datetime.now().strftime(
                "%Y-%m-%d"
            )
        )
    )

    connection.commit()

    connection.close()

    return jsonify({
        "message": "Expense added successfully."
    })


# =========================================
# SET BUDGET
# =========================================

@app.route(
    "/set-budget",
    methods=["POST"]
)
def set_budget():

    data = request.get_json(
        silent=True
    ) or {}

    amount_text = data.get(
        "amount",
        ""
    ).strip()

    if not amount_text:

        return jsonify({
            "error": "Budget amount is required."
        }), 400

    try:

        amount = float(
            amount_text
        )

    except ValueError:

        return jsonify({
            "error": "Please enter a valid amount."
        }), 400

    connection = get_connection()

    existing_budget = connection.execute(
        """
        SELECT id
        FROM budget
        WHERE id = 1
        """
    ).fetchone()

    if existing_budget:

        connection.execute(
            """
            UPDATE budget
            SET amount = ?
            WHERE id = 1
            """,
            (amount,)
        )

    else:

        connection.execute(
            """
            INSERT INTO budget (
                id,
                amount
            )
            VALUES (?, ?)
            """,
            (
                1,
                amount
            )
        )

    connection.commit()

    connection.close()

    return jsonify({
        "message": "Budget saved successfully."
    })


# =========================================
# ROBOTCHAT API
# =========================================

@app.route(
    "/chat",
    methods=["POST"]
)
def chat():

    try:

        data = request.get_json(
            silent=True
        ) or {}

        user_input = data.get(
            "message",
            ""
        ).strip()

        if not user_input:

            return jsonify({
                "response": (
                    "Please enter a message."
                )
            })

        tool_response = tool_router.run(
            user_input
        )

        if tool_response:

            response = tool_response

        else:

            response = (
                "Hello! How can I help you?"
            )

        return jsonify({
            "response": response
        })

    except Exception as error:

        print(
            "CHAT ERROR:",
            error
        )

        return jsonify({
            "response": (
                "Sorry, RobotChat could not "
                "process that message."
            )
        })

# =========================================
# RAREMOTION LABS WEBSITE
# =========================================

WEBSITE_FOLDER = os.path.join(
    os.path.dirname(__file__),
    "website"
)


@app.route("/labs")
def labs_home():

    return send_from_directory(
        WEBSITE_FOLDER,
        "index.html"
    )


@app.route("/labs/")
def labs_home_slash():

    return send_from_directory(
        WEBSITE_FOLDER,
        "index.html"
    )


@app.route("/labs/about")
def labs_about():

    return send_from_directory(
        WEBSITE_FOLDER,
        "about.html"
    )


@app.route("/labs/projects")
def labs_projects():

    return send_from_directory(
        WEBSITE_FOLDER,
        "projects.html"
    )


@app.route("/labs/services")
def labs_services():

    return send_from_directory(
        WEBSITE_FOLDER,
        "services.html"
    )


@app.route("/labs/contact")
def labs_contact():

    return send_from_directory(
        WEBSITE_FOLDER,
        "contact.html"
    )


@app.route("/labs/<path:filename>")
def labs_files(filename):

    return send_from_directory(
        WEBSITE_FOLDER,
        filename
    )

# =========================================
# START APPLICATION
# =========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )
