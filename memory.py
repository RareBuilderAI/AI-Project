import json


class Memory:

    def __init__(self):

        self.file_name = "robot_memory.json"
        self.memory = self.load_memory()


    def load_memory(self):

        try:

            with open(self.file_name, "r") as file:

                return json.load(file)

        except FileNotFoundError:

            return {}


    def save_memory(self):

        with open(self.file_name, "w") as file:

            json.dump(
                self.memory,
                file,
                indent=4
            )


    def save_user(self, name, goal):

        self.memory["name"] = name
        self.memory["goal"] = goal

        self.save_memory()


    def show_memory(self):

        if not self.memory:

            return "No memory saved."


        return (
            f"User: {self.memory['name']}\n"
            f"Goal: {self.memory['goal']}"
        )