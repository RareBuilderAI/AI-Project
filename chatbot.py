import os

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

TOKEN = os.getenv("8944033330:AAFLtMgKrsbviSlPvBSCSePJTmgPk31qzbk")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I'm Raremotion Lab's RobotChat 🤖\n"
        "What's your name?"
    )


async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    user_input = update.message.text.strip()
    message = user_input.lower()

    if message in ["exit", "quit", "bye"]:
        await update.message.reply_text(
            "RobotChat: Goodbye! 👋"
        )
        return

    if "what is your name" in message:
        await update.message.reply_text(
            "RobotChat: My name is RobotChat."
        )
        return

    if "what is my name" in message:
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

    response = ask_ai(user_input)

    await update.message.reply_text(
        f"RobotChat: {response}"
    )


def main():
    app = Application.builder().token(TOKEN).build()

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

    app.run_polling()


if __name__ == "__main__":
    main()