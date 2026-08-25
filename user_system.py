import json


class UserSystem:

    def __init__(self):

        self.file_name = "user_profile.json"
        self.user = self.load_user()


    def load_user(self):

        try:

            with open(self.file_name, "r") as file:

                return json.load(file)

        except FileNotFoundError:

            return {}


    def save_user(self):

        with open(self.file_name, "w") as file:

            json.dump(
                self.user,
                file,
                indent=4
            )


    def create_profile(self, name, goal):

        self.user = {
            "name": name,
            "goal": goal,
            "projects": [],
            "progress": "0/18 projects completed"
        }

        self.save_user()

        return "👤 User profile created successfully!"


    def add_project(self, project):

        self.user["projects"].append(project)

        self.save_user()

        return f"Project added: {project}"


    def show_profile(self):

        if not self.user:

            return "No user profile found."


        profile = (
            "👤 User Profile:\n\n"
            f"Name: {self.user['name']}\n"
            f"Goal: {self.user['goal']}\n\n"
            "Projects:\n"
        )


        for project in self.user["projects"]:

            profile += f"- {project}\n"


        profile += (
            f"\nProgress: {self.user['progress']}"
        )


        return profile
