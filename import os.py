import os
import asyncio
from datetime import datetime

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from memory import remember, recall
from ai_brain import ask_ai


load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


schedule = {
    "16:25": "Good morning Yhomi. Time to start your morning loop.",
    "08:00": "Gym time.",
    "09:30": "Shower, brush your teeth and have your healthy breakfast.",
    "10:30": "Back to the lab. Time to build.",
    "21:00": "Time to slow down and rest.",
}


CHAT_ID_FILE = "telegram_chat_id.txt"


def get_chat_id():
    try:
        with open(CHAT_ID_FILE, "r") as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return None


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    with open(CHAT_ID_FILE, "w") as file:
        file.write(str(chat_id))

    await update.message.reply_text(
        "Hello! I'm Raremotion Lab's RobotChat 🤖"
    )


async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    chat_id = update.effective_chat.id

    with open(CHAT_ID_FILE, "w") as file:
        file.write(str(chat_id))

    user_input = update.message.text.strip()
    message = user_input.lower()

    if message in ["exit", "quit", "bye"]:
        await update.message.reply_text(
            "RobotChat: Goodbye! 👋"
        )
        return

    if (
        "what is your name" in message
        or "what's your name" in message
    ):
        await update.message.reply_text(
            "RobotChat: My name is RobotChat."
        )
        return

    if (
        "what is my name" in message
        or "what's my name" in message
    ):
        name = recall("name")

        if name:
            await update.message.reply_text(
                f"RobotChat: Your name is {name}."
            )
        else:
            await update.message.reply_text(
                "RobotChat: I don't know your name yet."
            )

        return

    if message.startswith("my name is "):
        name = user_input[11:].strip()

        if name:
            remember("name", name)

            await update.message.reply_text(
                f"Nice to meet you, {name}! 👋"
            )

        return

    if (
        "what am i working on" in message
        or "what is my project" in message
    ):
        await update.message.reply_text(
            "You're working on RobotChat."
        )
        return

    response = ask_ai(user_input)

    await update.message.reply_text(
        f"RobotChat: {response}"
    )


async def reminder_scheduler(application):
    reminded_times = set()

    while True:
        current_time = datetime.now().strftime("%H:%M")

        if (
            current_time in schedule
            and current_time not in reminded_times
        ):
            chat_id = get_chat_id()

            if chat_id is not None:
                await application.bot.send_message(
                    chat_id=chat_id,
                    text=f"🔔 REMINDER: {schedule[current_time]}"
                )

                print(
                    "🔔 Telegram reminder sent:",
                    schedule[current_time]
                )

                reminded_times.add(current_time)

        if current_time not in schedule:
            reminded_times.clear()

        await asyncio.sleep(30)


async def post_init(application):
    asyncio.create_task(
        reminder_scheduler(application)
    )


def main():
    app = (
        Application.builder()
        .token(TOKEN)
        .post_init(post_init)
        .build()
    )

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )

    print("RobotChat Telegram bot is running...")
    print("🔔 Telegram reminder scheduler is running...")

    app.run_polling()


if __name__ == "__main__":
    main()