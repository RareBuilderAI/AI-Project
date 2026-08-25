from tool_router import ToolRouter


class RobotChatApp:

    def __init__(self):

        self.router = ToolRouter()


    def start(self):

        print(
            "🤖 RobotChat: Hello Yhomi. How can I help?"
        )


        while True:

            user = input("\nYou: ")


            if user.lower() == "exit":

                print(
                    "RobotChat closed 👋"
                )

                break


            response = self.router.run(user)


            print(
                "\nRobotChat:"
            )

            print(response)
