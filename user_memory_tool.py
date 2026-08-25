import json
import os


class UserMemoryTool:

    def __init__(self):
        self.file = "user_memory.json"


    def save_user(self, name, goal):

        data = {
            "name": name,
            "goal": goal
        }

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

        return "👤 User information saved successfully!"


    def get_user(self):

        if not os.path.exists(self.file):
            return "No user information found."

        with open(self.file, "r") as f:
            data = json.load(f)

        return (
            f"User: {data['name']}\n"
            f"Goal: {data['goal']}"
        )
