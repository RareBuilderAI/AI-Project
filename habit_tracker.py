habits = {}

while True:
    print("\nHabit Tracker 📅")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter habit name: ")

        habits[name] = 0

        print("Habit added! ✅")

    elif choice == "2":
        print("\nYour Habits:")

        for habit, count in habits.items():
            print(habit, ":", count, "days")

    elif choice == "3":
        name = input("Which habit did you complete? ")

        if name in habits:
            habits[name] += 1
            print("Habit completed! 🎉")
        else:
            print("Habit not found.")

    elif choice == "4":
        print("Habit Tracker closed 👋")
        break

    else:
        print("Invalid option")