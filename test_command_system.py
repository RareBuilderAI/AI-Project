from robotchat_core import RobotChat
from command_system import CommandSystem


robot = RobotChat()

commands = CommandSystem(robot)


print(
    commands.process("about")
)


print()


print(
    commands.process("brand")
)


print()


print(
    commands.process("tools")
)
