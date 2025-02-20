import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes

# Access the bot token from the environment variable
TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")

if not TOKEN:
    raise ValueError("Bot token is missing or invalid")


async def handle_any_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user = update.message.from_user
    username = user.username if user.username else "No username"

    # Create a detailed reply message with all the data
    reply_message = f"Message Details:\n\n"
    reply_message += f"User: @{username}\n\n"
    # Include the full Update data as a dictionary
    reply_message += f"Full Update Data: {update.to_json()}"  # Full data in dictionary format

    # Reply with all the details
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
