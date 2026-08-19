class User:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal

    def introduce(self):
        print("Name:", self.name)
        print("Goal:", self.goal)

    def update_goal(self, new_goal):
        self.goal = new_goal
        print("Goal updated!")


user1 = User("Yhomi", "Learn Python")

user1.introduce()

user1.update_goal("Build AI")

user1.introduce()