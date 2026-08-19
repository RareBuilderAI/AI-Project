import datetime

memory = {
    "name": "Yhomi",
    "project": "RobotChat"
}

routine = {
    "Morning": "Pray, gym, shower, breakfast",
    "Day": "Lab and build projects",
    "Night": "Rest and review progress"
}

reminders = {
    "07:00": "Morning routine",
    "09:30": "Breakfast",
    "10:30": "Build and learn",
    "21:00": "Rest"
}


print("🤖 Personal Assistant Started")

print(f"Welcome back, {memory['name']} 🚀")

while True:

    print("\nWhat do you want to know?")
    print("1. My routine")
    print("2. My reminders")
    print("3. My project")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        print("\nDaily Routine:")
        for time, task in routine.items():
            print(time, ":", task)

    elif choice == "2":
        print("\nReminders:")
        for time, reminder in reminders.items():
            print(time, ":", reminder)

    elif choice == "3":
        print("Current Project:", memory["project"])

    elif choice == "4":
        print("Assistant shutting down 👋")
        break

    else:
        print("Invalid choice")