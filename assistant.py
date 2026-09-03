from memory import Memory
from history import History
from personality import Personality
from knowledge import Knowledge
from router import Router
from tools import Tools
from status import Status
from tool_router import ToolRouter
from intent_router import IntentRouter
from ai_brain import AIBrain
from system_status import SystemStatus


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
        self.tool_router = ToolRouter()
        self.intent_router = IntentRouter()
        self.ai_brain = AIBrain()
        self.system_status = SystemStatus()

        self.guessing_game_active = False
        self.quiz_active = False
        self.contact_active = False

        self.setup_commands()


    def greet(self, user):

        print(
            self.name,
            "says: Hello",
            user.name
        )


    def remember(self, key, value):

        self.memory.remember(
            key,
            value
        )


    def recall(self, key):

        return self.memory.recall(key)


    def save_user(self, name, goal):

        return self.memory.save_user(
            name,
            goal
        )


    def show_available_tools(self):

        return self.tool_router.show_tools()


    def save_history(self, user_message, bot_message):

        self.history.add(
            user_message,
            bot_message
        )


    def setup_commands(self):

        self.router.add(
            "hello",
            lambda: "Hello! How can I help you?"
        )

        self.router.add(
            "goal",
            lambda: (
                "Your goal is to build AI "
                "and automation systems."
            )
        )

        self.router.add(
            "who are you",
            self.personality.about
        )


    def respond(self, message):

        command = message.lower().strip()


        # -----------------------------
        # Active Number Guessing Game
        # -----------------------------

        if self.guessing_game_active:

            response = self.tool_router.robot_tools.guess(
                command
            )

            if "Correct!" in response:

                self.guessing_game_active = False

            self.save_history(
                command,
                response
            )

            return response


        # -----------------------------
        # Active Quiz
        # -----------------------------

        if self.quiz_active:

            response = self.tool_router.robot_tools.answer_quiz(
                command
            )

            if "Quiz finished" in response:

                self.quiz_active = False

            self.save_history(
                command,
                response
            )

            return response


        # -----------------------------
        # Active Contact Book
        # -----------------------------

        if self.contact_active:

            response = self.tool_router.robot_tools.add_contact(
                command
            )

            self.contact_active = False

            self.save_history(
                command,
                response
            )

            return response


        # -----------------------------
        # Normal Commands
        # -----------------------------

        route = self.router.run(command)

        if route:

            response = route

            self.save_history(
                command,
                response
            )

            return response


        # -----------------------------
        # Tool Router
        # -----------------------------

        tool_response = self.tool_router.run(
            command
        )

        if tool_response:

            response = tool_response


            if command in [
                "start guessing game",
                "guessing game",
                "play guessing game"
            ]:

                self.guessing_game_active = True


            elif command in [
                "start quiz",
                "quiz",
                "play quiz",
                "start quiz game"
            ]:

                self.quiz_active = True


            elif command in [
                "add contact",
                "new contact"
            ]:

                self.contact_active = True


            self.save_history(
                command,
                response
            )

            return response


        # -----------------------------
        # Intent Router
        # -----------------------------

        intent = self.intent_router.detect(
            command
        )

        if intent:

            response = self.handle_intent(
                intent,
                command
            )

            self.save_history(
                command,
                response
            )

            return response


        # -----------------------------
        # AI Brain
        # -----------------------------

        response = self.ai_brain.think(
            command,
            memory=self.memory,
            history=self.history
        )

        self.save_history(
            command,
            response
        )

        return response


    def handle_intent(self, intent, command):

        if intent == "calculator":

            return self.calculator_response(
                command
            )


        if intent == "todo":

            return self.tool_router.todo.view_tasks()


        if intent == "weather":

            return self.tool_router.weather.get_weather(
                "Lagos"
            )


        if intent == "crypto":

            return self.tool_router.crypto.show_portfolio()


        if intent == "news":

            return self.tool_router.news.get_news()


        if intent == "brand":

            return self.tool_router.brand.about_brand()


        if intent == "support":

            return self.tool_router.support.answer(
                command
            )


        if intent == "expense":

            return self.tool_router.expense.view_expenses()


        if intent == "system_status":

            return self.system_status.show()


        if intent == "memory":

            return self.memory.show_memory()


        return (
            "I understand the request, "
            "but I don't know how to handle it yet."
        )


    def calculator_response(self, command):

        return self.tool_router.calculator.calculate(
            command
        )

