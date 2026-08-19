class Router:
    def __init__(self):
        self.commands = {}

    def add(self, name, function):
        self.commands[name] = function

    def run(self, command):
        if command in self.commands:
            return self.commands[command]()

        return None