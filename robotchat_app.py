from robotchat_core import RobotChat


class RobotChatApp:

    def __init__(self):

        self.robot = RobotChat()


    def start(self):

        print(self.robot.introduce())

        while True:

            message = input("You: ").strip()

            if not message:

                continue

            if message.lower() in ["quit", "exit", "bye"]:

                print("RobotChat closed 👋")

                break

            response = self.robot.respond(message)

            print(f"RobotChat: {response}")


if __name__ == "__main__":

    app = RobotChatApp()

    app.start()
