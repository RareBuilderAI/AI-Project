class User:
    def __init__(self, name):
        self.name = name


class Memory:
    def __init__(self):
        self.data = {}

    def remember(self, key, value):
        self.data[key] = value

    def recall(self, key):
        return self.data.get(key)


class Assistant:
    def __init__(self, name):
        self.name = name
        self.memory = Memory()

    def greet(self, user):
        print(self.name, "says: Hello", user.name)

    def remember_user_goal(self, goal):
        self.memory.remember("goal", goal)

    def show_goal(self):
        print("User goal:", self.memory.recall("goal"))


user = User("Yhomi")

robot = Assistant("RobotChat")

robot.greet(user)

robot.remember_user_goal("Build AI")

robot.show_goal()