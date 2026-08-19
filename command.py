class Command:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def execute(self):
        return self.action()