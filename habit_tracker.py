habits = {}


while True:

    print("\n🔥 Habit Tracker")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Mark Habit Complete")
    print("4. Delete Habit")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        habit = input("Enter habit name: ").strip()

        if not habit:
            print("Habit name is required.")
            continue

        if habit in habits:
            print("Habit already exists.")
            continue

        habits[habit] = False

        print("Habit added! ✅")

    elif choice == "2":

        print("\nYour Habits:")

        if not habits:
            print("No habits added yet.")

        else:
            for habit, completed in habits.items():

                if completed:
                    print("✅", habit)
                else:
                    print("❌", habit)

    elif choice == "3":

        habit = input(
            "Enter habit name to complete: "
        ).strip()

        if habit in habits:

            habits[habit] = True

            print("Habit marked complete! 🎉")

        else:
            print("Habit not found.")

    elif choice == "4":

        habit = input(
            "Enter habit name to delete: "
        ).strip()

        if habit in habits:

            del habits[habit]

            print("Habit deleted.")

        else:
            print("Habit not found.")

    elif choice == "5":

        print("Habit Tracker closed 👋")
        break

    else:

        print("Invalid option.")
