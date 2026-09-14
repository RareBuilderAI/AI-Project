import json

print("⚙️ Motion Engine")
print("Motion Engine is ready.")

DATA_FILE = "motions.json"


def load_motions():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_motions(motions):
    with open(DATA_FILE, "w") as file:
        json.dump(motions, file, indent=4)


def run_motion(motion, steps):
    print(f"\nStarting: {motion}")

    for number, step in enumerate(steps, start=1):
        print(f"{number}. → {step}")

    print("\nMotion completed! 🚀")


def create_motion(motions):
    motion = input("\nWhat motion do you want to create? ")

    if motion in motions:
        print("\nThat motion already exists.")
        return

    steps = []

    print("\nAdd the steps for this motion.")
    print("Type 'done' when you have finished.\n")

    while True:
        step = input("Add a step: ")

        if step.lower() == "done":
            break

        if step.strip():
            steps.append(step)

    if steps:
        motions[motion] = steps
        save_motions(motions)
        print("\nMotion saved! 💾")
    else:
        print("\nNo steps were added. Motion cancelled.")


def view_motions(motions):
    if not motions:
        print("\nNo motions have been saved yet.")
        return

    print("\n📋 Saved Motions:")

    for motion in motions:
        print(f"→ {motion}")


def update_motion(motions):
    motion = input("\nWhat motion do you want to edit? ")

    if motion not in motions:
        print("\nMotion not found.")
        return

    while True:
        print(f"\n⚙️ Editing: {motion}")
        print("\nCurrent steps:")

        for number, step in enumerate(motions[motion], start=1):
            print(f"{number}. {step}")

        print("\nWhat do you want to do?")
        print("1. Add a step")
        print("2. Remove a step")
        print("3. Change a step")
        print("4. Finish editing")

        choice = input("\nChoose an option: ")

        if choice == "1":
            step = input("\nEnter the new step: ")

            if step.strip():
                motions[motion].append(step)
                save_motions(motions)
                print("\nStep added! ➕")
            else:
                print("\nEmpty step was not added.")

        elif choice == "2":
            if not motions[motion]:
                print("\nThere are no steps to remove.")
                continue

            try:
                number = int(input("\nEnter the step number to remove: "))

                if 1 <= number <= len(motions[motion]):
                    removed_step = motions[motion].pop(number - 1)
                    save_motions(motions)
                    print(f"\nRemoved: {removed_step} 🗑️")
                else:
                    print("\nInvalid step number.")

            except ValueError:
                print("\nPlease enter a number.")

        elif choice == "3":
            if not motions[motion]:
                print("\nThere are no steps to change.")
                continue

            try:
                number = int(input("\nEnter the step number to change: "))

                if 1 <= number <= len(motions[motion]):
                    new_step = input("Enter the new step: ")

                    if new_step.strip():
                        old_step = motions[motion][number - 1]
                        motions[motion][number - 1] = new_step
                        save_motions(motions)

                        print(f"\nChanged: {old_step}")
                        print(f"To: {new_step} 🔄")
                    else:
                        print("\nEmpty step was not saved.")
                else:
                    print("\nInvalid step number.")

            except ValueError:
                print("\nPlease enter a number.")

        elif choice == "4":
            print("\nFinished editing.")
            break

        else:
            print("\nInvalid option. Choose 1-4.")


def delete_motion(motions):
    motion = input("\nWhat motion do you want to delete? ")

    if motion in motions:
        del motions[motion]
        save_motions(motions)
        print("\nMotion deleted! 🗑️")
    else:
        print("\nMotion not found.")


def menu():
    motions = load_motions()

    while True:
        print("\n" + "=" * 30)
        print("⚙️ MOTION ENGINE")
        print("=" * 30)

        print("1. Run a motion")
        print("2. Create a motion")
        print("3. View saved motions")
        print("4. Edit a motion")
        print("5. Delete a motion")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            motion = input("\nWhat motion do you want to run? ")

            if motion in motions:
                run_motion(motion, motions[motion])
            else:
                print("\nMotion not found.")

        elif choice == "2":
            create_motion(motions)

        elif choice == "3":
            view_motions(motions)

        elif choice == "4":
            update_motion(motions)

        elif choice == "5":
            delete_motion(motions)

        elif choice == "6":
            print("\nMotion Engine shutting down. 👋")
            break

        else:
            print("\nInvalid option. Choose 1-6.")


menu()
