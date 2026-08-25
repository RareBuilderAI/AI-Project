from robotchat_core import RobotChat


robot = RobotChat()


print(robot.introduce())


print(
    robot.save_user(
        "Yhomi",
        "Build AI and automation systems"
    )
)


print(
    robot.show_user()
)
