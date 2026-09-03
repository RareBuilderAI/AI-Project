class IntentRouter:

    def detect(self, command):

        command = command.lower().strip()


        if any(word in command for word in [
            "calculate",
            "calculator",
            "add",
            "subtract",
            "multiply",
            "divide"
        ]):

            return "calculator"


        if any(word in command for word in [
            "todo",
            "to-do",
            "task",
            "tasks"
        ]):

            return "todo"


        if any(word in command for word in [
            "weather",
            "temperature",
            "rain",
            "forecast"
        ]):

            return "weather"


        if any(word in command for word in [
            "crypto",
            "bitcoin",
            "portfolio"
        ]):

            return "crypto"


        if any(word in command for word in [
            "news",
            "headlines"
        ]):

            return "news"


        if any(word in command for word in [
            "brand",
            "raremotion",
            "company"
        ]):

            return "brand"


        if any(word in command for word in [
            "support",
            "help"
        ]):

            return "support"


        if any(word in command for word in [
            "expense",
            "expenses",
            "spending"
        ]):

            return "expense"


        if any(word in command for word in [
            "status",
            "system status"
        ]):

            return "system_status"


        if any(word in command for word in [
            "memory",
            "remember",
            "recall",
            "what do you remember"
        ]):

            return "memory"


        if any(word in command for word in [
            "start guessing game",
            "guessing game",
            "number guessing",
            "guess a number"
        ]):

            return "guessing_game"


        if any(word in command for word in [
            "start quiz",
            "quiz game",
            "take a quiz"
        ]):

            return "quiz"


        if any(word in command for word in [
            "password",
            "generate password",
            "create password"
        ]):

            return "password"


        if any(word in command for word in [
            "add contact",
            "view contacts",
            "contact book",
            "search contact",
            "delete contact"
        ]):

            return "contact"


        if any(word in command for word in [
            "add habit",
            "view habits",
            "complete habit",
            "habit tracker",
            "habit"
        ]):

            return "habit"


        return None
