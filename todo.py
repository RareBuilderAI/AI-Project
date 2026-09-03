import json
import os


FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []

    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    tasks = load_tasks()

    tasks.append({
        "task": task,
        "completed": False
    })

    save_tasks(tasks)

    return f"Task added! ✅ {task}"


def show_tasks():
    tasks = load_tasks()

    if not tasks:
        return "No tasks yet."

    result = "📝 Your Tasks:\n\n"

    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else "❌"
        result += f"{index}. {task['task']} {status}\n"

    return result.strip()


def complete_task(number):
    tasks = load_tasks()

    index = int(number) - 1

    if index < 0 or index >= len(tasks):
        return "That task number does not exist."

    tasks[index]["completed"] = True
    save_tasks(tasks)

    return f"Task completed! 🎉 {tasks[index]['task']}"


def delete_task(number):
    tasks = load_tasks()

    index = int(number) - 1

    if index < 0 or index >= len(tasks):
        return "That task number does not exist."

    removed_task = tasks.pop(index)
    save_tasks(tasks)

    return f"Task deleted: {removed_task['task']} 🗑️"


def edit_task(number, new_task):
    tasks = load_tasks()

    index = int(number) - 1

    if index < 0 or index >= len(tasks):
        return "That task number does not exist."

    tasks[index]["task"] = new_task
    save_tasks(tasks)

    return f"Task updated! ✏️ {new_task}"


def main():
    tasks = load_tasks()

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
            print(add_task(task))

        elif choice == "2":
            print(show_tasks())

        elif choice == "3":
            number = input("Which task is complete? ")
            print(complete_task(number))

        elif choice == "4":
            number = input("Which task do you want to delete? ")
            print(delete_task(number))

        elif choice == "5":
            number = input("Which task do you want to edit? ")
            new_task = input("Enter the new task: ")
            print(edit_task(number, new_task))

        elif choice == "6":
            print("To-Do App closed 👋")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
