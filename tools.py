class Tools:

    def __init__(self):
        self.available_tools = [
            "Calculator",
            "Weather",
            "Notes",
            "Tasks"
        ]


    def show_tools(self):

        return (
            "🛠️ Available Tools:\n\n"
            + "\n".join(self.available_tools)
        )


    def use_tool(self, tool_name):

        if tool_name in self.available_tools:

            return f"{tool_name} tool activated."

        return "Tool not found."
