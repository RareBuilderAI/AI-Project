from command import Command


hello_command = Command(
    "hello",
    lambda: "Hello Yhomi"
)

print(hello_command.execute())