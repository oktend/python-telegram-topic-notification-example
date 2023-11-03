# python-telegram-topic-notification-example

This repo demonstrate how to use https://github.com/oktend/python-telegram-handler for sending notifications to specific Telegram topics.

To get credentials for the bot see article: https://habr.com 

## Launch

to launch the project do following steps:
```bash
poetry install
poetry shell 

export TELEGRAM_NOTIFICATION_BOT_TOKEN=<bot_token>
export TELEGRAM_NOTIFICATION_CHAT_ID=<chat_id>
export TELEGRAM_MESSAGE_THREAD_ID=<message_id>

python main.py
```

You can change log level of messages that will be sent to Telegram: 
https://github.com/oktend/python-telegram-topic-notification-example/blob/main/main.py#L28
