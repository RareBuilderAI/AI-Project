import json


class TodoTool:

    def __init__(self):

        self.file = "tasks.json"


    def load_tasks(self):

        try:

            with open(self.file, "r") as f:

                return json.load(f)

        except FileNotFoundError:

            return []


    def save_tasks(self, tasks):

        with open(self.file, "w") as f:

            json.dump(tasks, f, indent=4)


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

            return "No tasks found."


        result = "📋 Tasks:\n\n"


        for index, task in enumerate(tasks, 1):

            status = "✅" if task["completed"] else "⬜"

            result += f"{index}. {status} {task['task']}\n"


        return result
