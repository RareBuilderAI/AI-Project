from datetime import datetime


class Tools:

    def __init__(self):
        self.available_tools = [
            "Calculator",
            "Weather",
            "Notes",
            "Date",
        ]

    def get_date(self):
        return datetime.now().strftime("%Y-%m-%d")

    def calculate(self, expression):
        try:
            allowed = "0123456789+-*/(). "

            if not all(char in allowed for char in expression):
                return "Invalid calculation."

            return str(eval(expression))

        except:
            return "I cannot calculate that."

    def show_tools(self):
        return (
            "Available tools: Calculator, Weather, Notes, Date"
        )

    def use_tool(self, tool_name):

        if tool_name.lower() == "date":
            return self.get_date()

        return "Tool not found."
