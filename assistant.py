from memory import Memory
from history import History
from personality import Personality
from knowledge import Knowledge
from router import Router
from tools import Tools
from status import Status


class Assistant:
    def __init__(self, name):
        self.name = name
        self.memory = Memory()
        self.history = History()
        self.personality = Personality()
        self.knowledge = Knowledge()
        self.router = Router()
        self.tools = Tools()
        self.status = Status()

        self.setup_commands()

    def greet(self, user):
        print(self.name, "says: Hello", user.name)

    def remember(self, key, value):
        self.memory.remember(key, value)

    def recall(self, key):
        return self.memory.recall(key)

    def save_history(self, user_message, bot_message):
        self.history.add(user_message, bot_message)

    def setup_commands(self):
        self.router.add(
            "hello",
            lambda: "Hello! How can I help you?"
        )

        self.router.add(
            "goal",
            lambda: "Your goal is to build AI."
        )

        self.router.add(
            "who are you",
            self.personality.about
        )

        self.router.add(
            "date",
            self.tools.get_date
        )

        self.router.add(
            "status",
            self.status.check
        )

    def respond(self, message):
        command = message.lower()

        route = self.router.run(command)

        if route:
            return route

        if command == "/help":
            return "Commands: hello, goal, who are you, date, status, remember, recall, /history"

        elif command.startswith("remember"):
            parts = message.split(" ", 2)

            if len(parts) < 3:
                return "Use: remember key value"

            key = parts[1]
            value = parts[2]

            self.memory.remember(key, value)

            return f"I remembered your {key}: {value}"

        elif command.startswith("recall"):
            parts = message.split(" ", 1)

            if len(parts) < 2:
                return "Use: recall key"

            key = parts[1]
            value = self.memory.recall(key)

            if value:
                return f"I remember your {key}: {value}"

            return "I don't remember that yet."

        elif command == "/history":
            return str(self.history.show())

        elif command.startswith("calculate"):
            expression = message.replace("calculate", "").strip()

            try:
                return self.tools.calculate(expression)

            except:
                return "I cannot calculate that."

        answer = self.knowledge.search(message)

        if answer:
            return answer

        return "I don't understand yet."