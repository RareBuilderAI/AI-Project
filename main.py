from user import User
from assistant import Assistant


name = input("What is your name? ")

user = User(name)

robot = Assistant("RobotChat")

robot.remember("name", user.name)

robot.greet(user)
while True:
    message = input("You: ")

    if message.lower() == "exit":
        print("RobotChat: Goodbye!")
        break

    response = robot.respond(message)

    robot.save_history(message, response)

    print("RobotChat:", response)