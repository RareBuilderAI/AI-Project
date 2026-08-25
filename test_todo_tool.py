from todo_tool import TodoTool


todo = TodoTool()


print(
    todo.add_task(
        "Connect projects to RobotChat"
    )
)


print(
    todo.add_task(
        "Build Raremotion Labs website"
    )
)


print(
    todo.view_tasks()
)
