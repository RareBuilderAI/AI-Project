from memory import remember, recall
from ai_brain import ask_ai


print("RobotChat: What is your name?")

user_name = input("You: ")

remember("name", user_name)

print(f"Hello, {user_name}! Welcome to RobotChat.")


while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("RobotChat: Goodbye! 👋")
        break

    # User asking RobotChat's name
    if "what is your name" in user_input.lower():
        print("RobotChat: My name is RobotChat.")
        continue

    # User asking their own name
    if "what is my name" in user_input.lower():
        name = recall("name")

        if name:
            print(f"RobotChat: Your name is {name}.")
        else:
            print("RobotChat: I don't know your name yet.")
        continue

    # Send normal questions to AI brain
    response = ask_ai(user_input)

    print("RobotChat:", response)