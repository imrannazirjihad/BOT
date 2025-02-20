import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes

# Access the bot token from the environment variable
TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")

if not TOKEN:
    raise ValueError("Bot token is missing or invalid")


async def handle_any_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming messages."""
    if update.message.sticker:
        is_sticker = bool(update.message.sticker)
        is_video = 'video' in update.message.sticker.is_video  # Check if it's a video sticker
        is_animated = update.message.sticker.is_animated
        set_name = update.message.sticker.set_name
        reply_message = f"Message Details:\n\n"
        reply_message += f"isSticker: {is_sticker}\n"
        reply_message += f"isVideo: {is_video}\n"
        reply_message += f"isAnimated: {is_animated}\n"
        reply_message += f"Sticker Set Name: {set_name}\n"
        await update.message.reply_text(reply_message)


async def start_methode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the bot is started."""
    await update.message.reply_text("Hello! I'm your bot. Send any message and I'll reply with the details.")


# Vercel expects a handler function for each route
async def handler(request):
    """Handles incoming requests for the bot."""
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start_methode))
    application.add_handler(MessageHandler(None, handle_any_message))

    # We only run the bot on incoming requests (handled by Vercel's HTTP endpoint)
    update = Update.de_json(request.json, application.bot)
    await application.process_update(update)
    return "OK"
