# python-telegram-topic-notification-example

## see main.py line 28, there you can set the log level
## see main.py line 41-45, only alerts with choosen level (28 line) and higher will be sent to telegram chat

# to run main.py you should:
open console pressing ctrl + shift + ~ 

## then run commands
poetry install

poetry shell 

## then export credentials
export TELEGRAM_NOTIFICATION_BOT_TOKEN=<bot_token>

export TELEGRAM_NOTIFICATION_CHAT_ID=<chat_id>

export REPLY_TO_MESSAGE_ID=<message_id>


## then run main.py
python main.py