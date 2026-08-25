from user_memory_tool import UserMemoryTool


memory = UserMemoryTool()


print(
    memory.save_user(
        "Yhomi",
        "Build AI and automation systems"
    )
)


print(
    memory.get_user()
)
