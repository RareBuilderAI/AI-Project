class Knowledge:
    def __init__(self):
        self.data = {
            "python": "Python is a programming language used to build software, automation, and AI.",
            "ai": "AI means artificial intelligence. It allows computers to perform tasks that normally require human intelligence.",
            "robotchat": "RobotChat is an AI assistant system built by Yhomi."
        }

    def search(self, question):
        question = question.lower()

        for key in self.data:
            if key in question:
                return self.data[key]

        return None