import json

file_name = "tasks.json"

try:
    with open(file_name, "r") as file:
        tasks = json.load(file)

except:
    tasks = []


while True:

    print("\nTo-Do List ✅")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. Exit")

    choice = input("Choose an option: ")


    if choice == "1":

        task = input("Enter task: ")

        tasks.append({
            "task": task,
            "completed": False
        })

        with open(file_name, "w") as file:
            json.dump(tasks, file, indent=4)

        print("Task added! ✅")


    elif choice == "2":

        print("\nYour Tasks:")

        if not tasks:
            print("No tasks yet.")

        else:
            for index, task in enumerate(tasks):
                status = "✅" if task["completed"] else "❌"
                print(index + 1, task["task"], status)


    elif choice == "3":

        number = int(input("Which task is complete? "))

        tasks[number - 1]["completed"] = True

        with open(file_name, "w") as file:
            json.dump(tasks, file, indent=4)

        print("Task completed! 🎉")


    elif choice == "4":

        number = int(input("Which task do you want to delete? "))

        removed_task = tasks.pop(number - 1)

        with open(file_name, "w") as file:
            json.dump(tasks, file, indent=4)

        print("Task deleted:", removed_task["task"], "🗑️")


    elif choice == "5":

        number = int(input("Which task do you want to edit? "))

        new_task = input("Enter the new task: ")

        tasks[number - 1]["task"] = new_task

        with open(file_name, "w") as file:
            json.dump(tasks, file, indent=4)

        print("Task updated! ✏️")


    elif choice == "6":

        print("To-Do App closed 👋")
        break


    else:

        print("Invalid option")