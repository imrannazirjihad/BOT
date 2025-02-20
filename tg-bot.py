import os

from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes
from telegram.ext import filters

# Create the Flask app
app = Flask(__name__)

# Access the bot token from the environment variable
TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")

if not TOKEN:
    raise ValueError("Bot token is missing or invalid")

# Initialize the Telegram bot
application = Application.builder().token(TOKEN).build()


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


async def start_methode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the bot is started."""
    await update.message.reply_text(
        "Hello! I'm your bot. Send any message and I'll reply with the details.")


# Setup handlers for the bot
application.add_handler(CommandHandler("start", start_methode))
application.add_handler(MessageHandler(None, handle_any_message))


@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    """Webhook handler for Telegram bot."""
    json_str = request.get_data().decode('UTF-8')
    update = Update.de_json(json_str, application.bot)
    application.process_update(update)
    return 'OK'


if __name__ == '__main__':
    # Set up the webhook to your Telegram bot
    application.bot.set_webhook(url=os.getenv("WEBHOOK_URL"))
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
