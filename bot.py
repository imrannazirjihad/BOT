from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace with your actual bot token
TOKEN = "7306080010:AAGmtNN2Im3HARP1etHEiKJAxN00KQieh0s"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the bot is started."""
    await update.message.reply_text("Hello! I'm your bot.")

def main():
    """Start the bot and handle commands."""
    # Create the Application using the bot's token
    application = Application.builder().token(TOKEN).build()

    # Add a command handler to respond to '/start' command
    application.add_handler(CommandHandler("start", start))

    # Start polling and keep the bot running
    application.run_polling()

if __name__ == '__main__':
    main()
