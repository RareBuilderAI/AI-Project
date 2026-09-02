import sqlite3
from datetime import datetime

class LeadTool:
    def __init__(self):
        self.db_path = "finance.db"

    def init_db(self):
        connection = sqlite3.connect(self.db_path)
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                project_details TEXT,
                date TEXT
            )
            """
        )
        connection.commit()
        connection.close()

    def save_lead(self, name, email, details):
        connection = sqlite3.connect(self.db_path)
        connection.execute(
            """
            INSERT INTO leads (name, email, project_details, date)
            VALUES (?, ?, ?, ?)
            """,
            (name, email, details, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
        connection.commit()
        connection.close()
        return "✅ Lead captured successfully! I have notified the Raremotion Labs team."

    def view_leads(self):
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        leads = connection.execute("SELECT * FROM leads ORDER BY id DESC").fetchall()
        connection.close()

        if not leads:
            return "No leads captured yet."

        output = "📋 Captured Leads:\n"
        for lead in leads:
            output += f"- {lead['name']} ({lead['email']}): {lead['project_details']}\n"
        return output
