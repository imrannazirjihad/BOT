from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7306080010:AAGmtNN2Im3HARP1etHEiKJAxN00KQieh0s"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm your bot.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
