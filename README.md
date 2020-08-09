# Telegram-bot

## This bot is used to configure Telegram Bots commands

After registering your Bot with BotFather in Telegram ([Here's](https://core.telegram.org/bots) a link on how to do it) , you will be provided the Bot Token.

You can use it directly in OR you can also save it in a **.env** file and load it from the environment variable and then use it like this.
```
TOKEN = "your token here"
    OR
TOKEN = os.getenv('BOT_TOKEN') #loading from .env file

bot = telebot.TeleBot(token=TOKEN)
```

After that you can configure the commands depending on what you want to do.
```
@bot.message_handler(commands=['your_command_name_here']) 
def send_welcome(message):
    bot.reply_to(message, 'Welcome to our bot.. ')
```
>This is a simple example on how you can reply when a particular command is selected on the Bot. For more options you can check [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)

The code in Bot.py is written to Start and Stop an Azure Virtual Machine using an private API which is also stored in **.env** file.
