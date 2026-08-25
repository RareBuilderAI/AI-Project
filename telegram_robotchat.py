import os
from dotenv import load_dotenv

load_dotenv()

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from tool_router import ToolRouter
from robot_brain import RobotBrain


router = ToolRouter()
brain = RobotBrain(router)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤖 RobotChat is online. How can I help?"
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message.text.lower()

    print("USER SENT:", repr(message))

    response = brain.think(message)

    await update.message.reply_text(response)


def run_bot():

    app = Application.builder().token(
        os.getenv("TELEGRAM_TOKEN")
    ).build()

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT,
            chat
        )
    )

    print("🤖 RobotChat Telegram Bot running...")

    app.run_polling()


if __name__ == "__main__":
    run_bot()
