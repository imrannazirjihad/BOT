from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Replace with your actual bot token
TOKEN = "7306080010:AAGmtNN2Im3HARP1etHEiKJAxN00KQieh0s"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the bot is started."""
    await update.message.reply_text("Hello! I'm your bot.")

async def handle_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle stickers and show the sender's username."""
    sticker = update.message.sticker
    user = update.message.from_user
    username = user.username if user.username else "No username"
    # Send the sticker owner username to the chat
    await update.message.reply_text(f"Sticker sent by @{username}")

def main():
    """Start the bot and handle commands."""
    # Create the Application using the bot's token
    application = Application.builder().token(TOKEN).build()

    # Add a command handler to respond to '/start' command
    application.add_handler(CommandHandler("start", start))

    # Add a message handler to respond to stickers
    application.add_handler(MessageHandler(filters.Sticker, handle_sticker))

    # Start polling and keep the bot running
    application.run_polling()

if __name__ == '__main__':
    main()
