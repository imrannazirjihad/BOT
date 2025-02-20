from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace with your actual bot token
TOKEN = "YOUR_TELEGRAM_BOT_API_TOKEN"

def start(update: Update, context: CallbackContext):
    """Send a welcome message when the bot is started."""
    update.message.reply_text("Hello! I'm your bot.")

def main():
    """Start the bot and handle commands."""
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add a command handler to respond to '/start' command
    dispatcher.add_handler(CommandHandler("start", start))

    # Start polling and keep the bot running
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
