import json


class History:
    def __init__(self):
        self.file = "history.json"
        self.messages = self.load()

    def add(self, user_message, bot_message):
        self.messages.append({
            "user": user_message,
            "assistant": bot_message
        })
        self.save()

    def show(self):
        return self.messages

    def save(self):
        with open(self.file, "w") as file:
            json.dump(self.messages, file, indent=4)

    def load(self):
        try:
            with open(self.file, "r") as file:
                return json.load(file)
        except:
            return []