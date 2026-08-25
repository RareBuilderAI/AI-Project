from calculator import Calculator
from todo_tool import TodoTool
from weather_tool import WeatherTool
from crypto_tool import CryptoTool
from brand_tool import BrandTool
from customer_support_tool import CustomerSupportTool
from news_tool import NewsTool
from expense_tool import ExpenseTool
from user_memory_tool import UserMemoryTool


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
        self.memory = UserMemoryTool()


    def run(self, command):

        command = command.lower()


        if command == "help":

            return """
🤖 RobotChat Commands:

brand - About Raremotion Labs
tools - Show available tools
weather - Check weather
calculator - Calculator tool
todo - View tasks
crypto - View crypto portfolio
news - Latest news
expense - View expenses
memory - View user memory
"""


        if command == "brand":

            return self.brand.about_brand()


        if "weather" in command:

            return self.weather.get_weather("Lagos")


        if "news" in command:

            return self.news.get_news()


        if "calculator" in command:

            return "🧮 Calculator is ready."


        if "todo" in command:

            return self.todo.view_tasks()


        if "crypto" in command:

            return self.crypto.show_portfolio()


        if "expense" in command:

            return self.expense.view_expenses()


        if "memory" in command:

            return self.memory.get_user()


        if "support" in command:

            return self.support.answer("support")


        return "Command not recognized."