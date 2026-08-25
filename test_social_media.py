from social_media_assistant import SocialMediaAssistant


assistant = SocialMediaAssistant()


assistant.create_content(
    "TikTok",
    "Video",
    "AI",
    "Show how RobotChat works",
    "Building the future with AI 🤖"
)


assistant.create_content(
    "LinkedIn",
    "Post",
    "Python",
    "Share my coding journey",
    "Building AI projects step by step 🦾"
)


print(assistant.show_content())


print(
    assistant.edit_content(
        1,
        "AI is changing the future 🚀"
    )
)


print(assistant.show_content())


print(
    assistant.delete_content(2)
)


print(assistant.show_content())