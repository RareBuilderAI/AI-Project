import json


class TodoTool:

    def __init__(self):

        self.file = "tasks.json"


    def load_tasks(self):

        try:

            with open(self.file, "r") as f:

                return json.load(f)

        except (FileNotFoundError, json.JSONDecodeError):

            return []


    def save_tasks(self, tasks):

        with open(self.file, "w") as f:

            json.dump(
                tasks,
                f,
                indent=4
            )


    def add_task(self, task):

        tasks = self.load_tasks()

        tasks.append(
            {
                "task": task,
                "completed": False
            }
        )

        self.save_tasks(tasks)

        return "✅ Task added successfully!"


    def view_tasks(self):

        tasks = self.load_tasks()

        if not tasks:

            return "📋 No tasks found."


        result = "📋 Tasks:\n\n"


        for index, task in enumerate(tasks, 1):

            status = (
                "✅"
                if task["completed"]
                else "❌"
            )

            result += (
                f"{index}. {status} "
                f"{task['task']}\n"
            )


        return result


    def complete_task(self, task_number):

        tasks = self.load_tasks()

        try:

            index = int(task_number) - 1

        except ValueError:

            return "Please provide a valid task number."


        if index < 0 or index >= len(tasks):

            return "That task does not exist."


        tasks[index]["completed"] = True

        self.save_tasks(tasks)

        return (
            f"✅ Task completed: "
            f"{tasks[index]['task']}"
        )


    def delete_task(self, task_number):

        tasks = self.load_tasks()

        try:

            index = int(task_number) - 1

        except ValueError:

            return "Please provide a valid task number."


        if index < 0 or index >= len(tasks):

            return "That task does not exist."


        deleted_task = tasks.pop(index)

        self.save_tasks(tasks)

        return (
            f"🗑️ Task deleted: "
            f"{deleted_task['task']}"
        )
