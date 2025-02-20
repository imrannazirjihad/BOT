import os

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes

# Access the bot token from the environment variable
TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")

if not TOKEN:
    raise ValueError("Bot token is missing or invalid")


async def handle_any_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    is_sticker = bool(update.message.sticker.is_video)
    if is_sticker:
        is_video = bool(update.message.sticker)
        is_animated = bool(update.message.sticker.is_animated)
        set_name = update.message.sticker.set_name
        reply_message = f"Message Details:\n\n"
        reply_message += f"isVideo: {is_video}\n\n"
        reply_message += f"isSticker: {is_sticker}\n\n"
        reply_message += f"isAnimated: {is_animated}\n\n"
        reply_message += f"Name: {set_name}\n\n"
        await update.message.reply_text(reply_message)


def main_methode():
    # Create the Application using the bot's token
    application = Application.builder().token(TOKEN).build()

    # Response For '/start' command
    application.add_handler(CommandHandler("start", start_methode))

    # Add a message handler to respond to any message
    application.add_handler(MessageHandler(None, handle_any_message))

    # Start polling and keep the bot running
    application.run_polling()


async def start_methode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the bot is started."""
    await update.message.reply_text(
        "Hello! I'm your bot. Send any message and I'll reply with the details."
    )


if __name__ == '__main__':
    main_methode()
