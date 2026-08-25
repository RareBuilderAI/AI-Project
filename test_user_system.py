from user_system import UserSystem


user = UserSystem()


print(
    user.create_profile(
        "Yhomi",
        "Build AI and automation systems"
    )
)


print(
    user.add_project(
        "Personal Assistant"
    )
)


print(
    user.add_project(
        "Social Media Content Assistant"
    )
)


print(
    user.add_project(
        "Crypto Dashboard"
    )
)


print(
    user.show_profile()
)
