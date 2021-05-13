import logging 
from telegram.ext import Updater , CommandHandler , MessageHandler , Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update,context):
    update.message.reply_text("hi i am a test bot")

def error(update,error):
    gger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater("token" , use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start" , start))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
