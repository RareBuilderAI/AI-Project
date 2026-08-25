class Personality:
    def __init__(self):
        self.name = "RobotChat"
        self.creator = "Yhomi"
        self.mission = "Build AI and automation systems"

    def about(self):
        return f"I am {self.name}, built by {self.creator}. My mission is to {self.mission}."


robot = Personality()

print(robot.about())