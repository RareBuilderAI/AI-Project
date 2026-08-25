class CommandSystem:

    def __init__(self, robot):

        self.robot = robot


    def process(self, command):

        command = command.lower()


        if command == "brand":

            return self.robot.about_brand()


        elif command == "profile":

            return self.robot.show_profile()


        elif command == "tools":

            return self.robot.show_available_tools()


        elif command == "memory":

            return self.robot.show_user_memory()


        elif command == "about":

            return self.robot.introduce()


        else:

            return "Command not recognized."
