class RobotBrain:

    def __init__(self, router):

        self.router = router


    def think(self, message):

        message = message.lower()


        if "hello" in message:

            return "🤖 Hello Yhomi. RobotChat is online."


        if "spend" in message or "expense" in message:

            return self.router.run("expense")


        if "money" in message or "crypto" in message:

            return self.router.run("crypto")


        if "news" in message:

            return self.router.run("news")


        if "weather" in message:

            return self.router.run("weather")


        if "task" in message or "todo" in message:

            return self.router.run("todo")


        if "memory" in message:

            return self.router.run("memory")


        return self.router.run(message)
