from robot_tools import RobotTools


tools = RobotTools()


print(
    tools.use_calculator(
        "add",
        10,
        5
    )
)


print(
    tools.use_calculator(
        "multiply",
        10,
        5
    )
)
