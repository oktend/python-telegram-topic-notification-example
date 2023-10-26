import os
import logging
from telegram_handler.handlers import TelegramHandler
from telegram_handler.formatters import HtmlFormatter

"""
Configure logger: 
https://docs.python.org/3/howto/logging.html#configuring-logging
"""


log = logging.getLogger('main')

def init_logger(telegram_chat_token, telegram_chat_id, telegram_reply_to_message):

    log.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(levelname)s: %(message)s')

    stream_handler.setFormatter(formatter)

    log.addHandler(stream_handler)

    telegram_handler = TelegramHandler(level=logging.WARNING, token=telegram_chat_token, reply_to_message_id=telegram_reply_to_message, chat_id=telegram_chat_id)
    telegram_handler.setLevel(logging.WARNING) # logging.WARNING sets the log level you will recieve in telegram chat to level WARNING and higher

    formatter = HtmlFormatter()
    telegram_handler.setFormatter(formatter)

    log.addHandler(telegram_handler)

def main():
    init_logger(
        os.getenv("TELEGRAM_NOTIFICATION_BOT_TOKEN"),
        os.getenv("TELEGRAM_NOTIFICATION_CHAT_ID"),
        os.getenv("REPLY_TO_MESSAGE_ID"),
        )
    log.info(f"this message level: info") # When you run the script, only alerts with choosen level (line 28) and higher will be sent to telegram chat
    log.debug(f"this message level: debug")
    log.warning(f"this message level: warning")
    log.error(f"this message level: error")
    log.critical(f"this message level: critical")

if __name__ == "__main__":
    main()
