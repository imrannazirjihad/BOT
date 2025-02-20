import os
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from flask import Flask, request

# Access the bot token from the environment variable
TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

if not TOKEN:
    raise ValueError("Bot token is missing or invalid")

# Initialize Flask app
app = Flask(__name__)

# Telegram Bot setup
bot = Bot(token=TOKEN)

# Handle incoming messages
async def handle_any_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    is_sticker = bool(update.message.sticker.is_video) if update.message.sticker else False
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
    else:
        await update.message.reply_text("You sent a normal message!")

# Start command handler
async def start_methode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the bot is started."""
    await update.message.reply_text("Hello! I'm your bot. Send any message and I'll reply with the details.")

# Webhook route to handle updates
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = Update.de_json(json_str, bot)
    application = Application.builder().token(TOKEN).build()
    application.dispatcher.process_update(update)
    return "OK", 200

# Set up webhook
def set_webhook():
    bot.set_webhook(url=WEBHOOK_URL)

# Main entry point for the app
if __name__ == "__main__":
    set_webhook()  # Set the webhook when starting the server
    app.run(host="0.0.0.0", port=5000)
