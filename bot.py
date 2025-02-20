import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Access the bot token from the environment variable
TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")

if not TOKEN:
    raise ValueError("Bot token is missing or invalid")

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the bot is started."""
    await update.message.reply_text("Hello! I'm your bot.")

# Handle any incoming message and print the type
async def handle_any_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle any incoming message."""
    if update.message.text:
        message_type = 'text'
    elif update.message.sticker:
        message_type = 'sticker'
    elif update.message.photo:
        message_type = 'photo'
    else:
        message_type = 'unknown'

    # Do something with the message type, for example, print it
    print(f"Received a {message_type} message")

    # You can also send a response
    await update.message.reply_text(f"Message type: {message_type}")

# Handle stickers and show sender's username
async def handle_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle stickers and show the sender's username."""
    sticker = update.message.sticker
    user = update.message.from_user
    username = user.username if user.username else "No username"
    await update.message.reply_text(f"Sticker sent by @{username}")

# Main function to run the bot
def main():
    """Start the bot and handle commands."""
    # Create the Application using the bot's token
    application = Application.builder().token(TOKEN).build()

    # Add handlers for the bot
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT | filters.STICKER | filters.PHOTO, handle_any_message))
    application.add_handler(MessageHandler(filters.Sticker, handle_sticker))

    # Start polling and keep the bot running
    application.run_polling()

if __name__ == '__main__':
    main()
