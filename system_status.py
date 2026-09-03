class SystemStatus:

    def __init__(self):
        self.name = "RobotChat"
        self.version = "1.0"
        self.status = "Online"

    def show(self):
        return (
            f"🤖 {self.name}\n"
            f"Version: {self.version}\n"
            f"Status: {self.status}\n"
            "AI Brain: Online\n"
            "Memory: Online\n"
            "History: Online\n"
            "Intent Router: Online\n"
            "Tool Router: Online"
        )
