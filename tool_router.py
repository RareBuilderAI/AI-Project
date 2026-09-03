from calculator import Calculator
from todo_tool import TodoTool
from weather_tool import WeatherTool
from crypto_tool import CryptoTool
from brand_tool import BrandTool
from customer_support_tool import CustomerSupportTool
from news_tool import NewsTool
from expense_tool import ExpenseTool
from memory import Memory
from robot_tools import RobotTools


class ToolRouter:

    def __init__(self):

        self.calculator = Calculator()
        self.todo = TodoTool()
        self.weather = WeatherTool()
        self.crypto = CryptoTool()
        self.brand = BrandTool()
        self.support = CustomerSupportTool()
        self.news = NewsTool()
        self.expense = ExpenseTool()
        self.memory = Memory()
        self.robot_tools = RobotTools()


    def show_tools(self):

        return (
            "📝 To-Do List\n"
            "💰 Expense Tracker\n"
            "🧮 Calculator\n"
            "🎯 Number Guessing Game\n"
            "🧠 Quiz Game\n"
            "🔐 Password Generator\n"
            "📒 Contact Book\n"
            "🔥 Habit Tracker\n"
            "🌤️ Weather\n"
            "₿ Crypto Portfolio\n"
            "📰 News\n"
            "🏢 Raremotion Labs\n"
            "💬 Customer Support"
        )


    def run(self, command):

        command = command.strip()

        lower_command = command.lower()


        # --------------------------------
        # Show available tools
        # --------------------------------

        if lower_command in [
            "tools",
            "show tools",
            "available tools",
            "what can you do"
        ]:

            return self.show_tools()


        # --------------------------------
        # Number Guessing Game
        # --------------------------------

        if lower_command in [
            "start guessing game",
            "guessing game",
            "play guessing game"
        ]:

            return self.robot_tools.start_guessing_game()


        # --------------------------------
        # Quiz Game
        # --------------------------------

        if lower_command in [
            "start quiz",
            "quiz",
            "play quiz",
            "start quiz game"
        ]:

            return self.robot_tools.start_quiz()


        # --------------------------------
        # Contact Book
        # --------------------------------

        if lower_command in [
            "add contact",
            "new contact"
        ]:

            return (
                "📒 Contact Book\n"
                "Send the contact like this: name, phone"
            )


        if lower_command in [
            "view contacts",
            "show contacts",
            "contacts"
        ]:

            return self.robot_tools.view_contacts()


        # --------------------------------
        # Password Generator
        # --------------------------------

        if lower_command in [
            "generate password",
            "password generator",
            "create password"
        ]:

            return self.robot_tools.generate_password(12)


        # --------------------------------
        # Habit Tracker
        # --------------------------------

        if lower_command.startswith("add habit"):

            return self.robot_tools.handle_habit(
                lower_command
            )


        if lower_command.startswith("complete habit"):

            return self.robot_tools.handle_habit(
                lower_command
            )


        if lower_command in [
            "view habits",
            "show habits",
            "habits"
        ]:

            return self.robot_tools.handle_habit(
                "view habits"
            )


        # --------------------------------
        # Calculator
        # --------------------------------

        if lower_command.startswith("calculate"):

            return self.calculator.calculate(
                lower_command
            )


        # --------------------------------
        # To-Do List
        # --------------------------------

        if lower_command.startswith("add task"):

            task = command[8:].strip()

            if not task:

                return "Please provide a task."

            return self.todo.add_task(task)


        if lower_command in [
            "view tasks",
            "show tasks",
            "todo",
            "to-do"
        ]:

            return self.todo.view_tasks()


        # --------------------------------
        # Expense Tracker
        # --------------------------------

        if lower_command in [
            "view expenses",
            "show expenses",
            "expenses"
        ]:

            return self.expense.view_expenses()


        # --------------------------------
        # Weather
        # --------------------------------

        if lower_command in [
            "weather",
            "check weather",
            "weather today"
        ]:

            return self.weather.get_weather(
                "Lagos"
            )


        # --------------------------------
        # Crypto
        # --------------------------------

        if lower_command in [
            "crypto",
            "crypto portfolio",
            "show crypto"
        ]:

            return self.crypto.show_portfolio()


        # --------------------------------
        # News
        # --------------------------------

        if lower_command in [
            "news",
            "latest news",
            "show news"
        ]:

            return self.news.get_news()


        # --------------------------------
        # Brand
        # --------------------------------

        if lower_command in [
            "brand",
            "about brand",
            "raremotion labs"
        ]:

            return self.brand.about_brand()


        # --------------------------------
        # Customer Support
        # --------------------------------

        if lower_command.startswith("support"):

            return self.support.answer(
                command
            )


        return None
