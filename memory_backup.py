import json
import os


class Memory:

    def __init__(self):
        self.filename = "memory.json"
        self.memory = {}
        self.load_memory()

    def load_memory(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.memory = json.load(file)
            except (json.JSONDecodeError, OSError):
                self.memory = {}
        else:
            self.memory = {}

    def save_memory(self):
        with open(self.filename, "w") as file:
            json.dump(self.memory, file, indent=4)

    def save_user(self, name, goal):
        self.memory["name"] = name
        self.memory["goal"] = goal
        self.save_memory()

    def remember(self, key, value):
        self.memory[key] = value
        self.save_memory()

    def recall(self, key):
        return self.memory.get(key)

    def show_memory(self):
        if not self.memory:
            return "No memory saved."

        return (
            f"User: {self.memory.get('name', 'Unknown')}\n"
            f"Goal: {self.memory.get('goal', 'Not set')}"
        )