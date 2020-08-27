# Telegram-bot

## To understand the entire project please do read [my article](https://medium.com/@nihir_shah/managing-azure-instances-with-telegram-bot-using-python-part-2-f9a19923132d) on it.

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

The code in Bot.py is written to Start and Stop an Azure Virtual Machine using an private API whose URL are also stored in **.env** file and then called via the requests library in Python.
It's done in 3 steps
1. It checks whether the user who is trying to start or stop the server is whether authorised or not to do so and replies accoridngly to the user if not authorised.
2. It checks the current status of the Azure' VM and if it's the opposite then it calls the private URL to turn on or off the server.
3. If first two steps are validated then it sends a message to user that it is trying to Start/Stop the server and it may take some time.
4. On successfull response from the API then it replies to the user that the task has been completed.

###### This code is designed to run on the local machine & you can run the scirpt and try sending the command to get the desired reply.
##### If you are not planning to call any private API then you can host it on [PythonAnywhere](https://www.pythonanywhere.com/) so that you don't have to keep on running the script on your local machine.
##### If you want to call any API which is not whitelisted by PythonAnywhere then you will have to use [Heroku](https://heroku.com) by configuring it with flask to make it compatible to run.
