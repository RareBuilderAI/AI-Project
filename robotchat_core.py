from assistant import Assistant


class RobotChat:

    def __init__(self):

        self.assistant = Assistant("RobotChat")


    def introduce(self):

        return (
            "I am RobotChat, built by Yhomi. "
            "My mission is to Build AI and automation systems."
        )


    def about_brand(self):

        return (
            "🏢 Raremotion Labs\n"
            "Technology studio focused on AI, automation, "
            "software development, and digital systems."
        )


    def show_available_tools(self):

        return self.assistant.show_available_tools()


    def save_user(self, name, goal):

        return self.assistant.save_user(name, goal)


    def show_user(self):

        return self.assistant.memory.get_user()


    def remember(self, key, value):

        return self.assistant.remember(key, value)


    def recall(self, key):

        return self.assistant.recall(key)


    def respond(self, message):

        return self.assistant.respond(message)
