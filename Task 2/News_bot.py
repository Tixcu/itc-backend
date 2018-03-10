#!/usr/bin/env python
# -*- coding: utf-8 -*-


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import random
import os
import json

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def pynews(bot, update):
    """Send random news"""
    with open("vk_posts.json", "r") as file:
        str = file.read()
        db = json.loads(str)
        post_number = int(random.uniform(0,len(db)))
        # Printing first two rows
        update.message.reply_text(db[post_number]['text'].split('\n',2)[0]+'..')

        # Creating url from owner id and id of post in vk
        update.message.reply_text('https://vk.com/feed?w=wall%s_%s' % (db[post_number]['owner_id'],db[post_number]['id']))

    
def slava(bot, update):
    """Ignore this pls"""
    update.message.reply_text("Слава украине\nГероям слава")


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater('549665186:AAH9gt7nI_fBAP6dxWRvO-KSh9Io7D__bFQ')

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("pynews", pynews))
    dp.add_handler(CommandHandler("slava", slava))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
