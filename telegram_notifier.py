import requests
import os

class TelegramNotifier:
    def __init__(self):
        # These will be set as Environment Variables in Render for security
        self.token = os.environ.get("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    def send_notification(self, lead_name, lead_email, lead_details):
        if not self.token or not self.chat_id:
            print("Telegram credentials missing. Notification not sent.")
            return False

        message = (
            "🚨 *NEW LEAD CAPTURED!*\n\n"
            f"👤 *Name:* {lead_name}\n"
            f"📧 *Email:* {lead_email}\n"
            f"📝 *Project:* {lead_details}\n\n"
            "👉 Check the Command Center for more details!"
        )

        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }

        try:
            response = requests.post(url, json=payload)
            return response.status_code == 200
        except Exception as e:
            print(f"Telegram Error: {e}")
            return False
