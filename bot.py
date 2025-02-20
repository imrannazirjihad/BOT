import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes
# Access the bot token from the environment variable
TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

if not TOKEN:
    raise ValueError("Bot token is missing or invalid")
if not ETHERSCAN_API_KEY:
    raise ValueError("Etherscan API key is missing or invalid")

async def handle_any_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    is_sticker = bool(update.message.sticker)
    if is_sticker:
        is_video = bool(update.message.sticker.is_video)
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
        "Hello! I'm your bot. Send any message and I'll reply with the details."
    )

async def get_gas_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Fetch the gas price from Etherscan and send it to the user."""
    url = f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "1":
        gas_price = data["result"]
        reply_message = f"Current Gas Prices:\n\n"
        reply_message += f"Low: {gas_price['SafeGasPrice']} Gwei\n"
        reply_message += f"Standard: {gas_price['ProposeGasPrice']} Gwei\n"
        reply_message += f"High: {gas_price['FastGasPrice']} Gwei\n"
        await update.message.reply_text(reply_message)
    else:
        await update.message.reply_text("Failed to fetch gas data. Please try again later.")


#Main Code HERE
def main_methode():
    # Create the Application using the bot's token
    application = Application.builder().token(TOKEN).build()

    # Response For '/start' command
    application.add_handler(CommandHandler("start", start_methode))

    # Response For '/gas' command
    application.add_handler(CommandHandler("gas", get_gas_data))

    # Add a message handler to respond to any message
    application.add_handler(MessageHandler(None, handle_any_message))

    # Start polling and keep the bot running
    application.run_polling()

if __name__ == '__main__':
    main_methode()

