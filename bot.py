import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Access the bot token from the environment variable
TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")

if not TOKEN:
    raise ValueError("Bot token is missing or invalid")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the bot is started."""
    await update.message.reply_text("Hello! I'm your bot. Send a text or a sticker.")

# Handle only text messages
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle text messages."""
    text = update.message.text
    user = update.message.from_user
    username = user.username if user.username else "No username"
    await update.message.reply_text(f"Text message received from @{username}: {text}")

# Handle only sticker messages
async def handle_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle stickers and show the sender's username."""
    sticker = update.message.sticker
    user = update.message.from_user
    username = user.username if user.username else "No username"
    await update.message.reply_text(f"Sticker sent by @{username}")

# Handle only photo messages
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle photo messages."""
    photo = update.message.photo
    user = update.message.from_user
    username = user.username if user.username else "No username"
    await update.message.reply_text(f"Photo sent by @{username}")

def main():
    """Start the bot and handle commands."""
    # Create the Application using the bot's token
    application = Application.builder().token(TOKEN).build()

    # Add a command handler to respond to '/start' command
    application.add_handler(CommandHandler("start", start))

    # Add a message handler to respond to text messages
    application.add_handler(MessageHandler(filters.TEXT, handle_text))

    # Add a message handler to respond to sticker messages
    # application.add_handler(MessageHandler(filters.STICKER, handle_sticker))

    # Add a message handler to respond to photo messages
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    # Start polling and keep the bot running
    application.run_polling()

if __name__ == '__main__':
    main()
