from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

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

# Add this handler to your bot (if not already done)
application.add_handler(MessageHandler(filters.TEXT | filters.STICKER | filters.PHOTO, handle_any_message))
