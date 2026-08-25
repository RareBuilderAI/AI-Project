from user_memory_tool import UserMemoryTool


class RobotChat:

    def __init__(self):

        self.name = "RobotChat"
        self.owner = "Yhomi"
        self.goal = "Build AI and automation systems"

        self.memory = UserMemoryTool()


    def introduce(self):

        return (
            f"I am {self.name}, built by {self.owner}. "
            f"My mission is to {self.goal}."
        )


    def save_user(self, name, goal):

        return self.memory.save_user(
            name,
            goal
        )


    def show_user(self):

        return self.memory.get_user()
