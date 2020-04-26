import logging, random, os

from telegram.ext import Updater, MessageHandler, Filters

from mongobot.custom_filters import filter_twitter_url
from mongobot.handlers import start, response
from mongobot.mongodb import load_commands, new_connection

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    updater = Updater(token=os.environ.get('TOKEN_BOT'), use_context=True)
    new_connection()

    dispatcher = updater.dispatcher
    
    load_commands(dispatcher)
    dispatcher.add_handler(MessageHandler(filter_twitter_url, response))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()