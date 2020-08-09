import telebot
import requests , os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

bot_token = TOKEN
bot = telebot.TeleBot(token=bot_token)
AUTHORISED_USERS = os.getenv('AUTHORISED_USERS')

authorized_users = AUTHORISED_USERS.split(",")
for index,element in enumerate(authorized_users):
    authorized_users[index] = element.strip()

@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, 'Welcome to our bot.. I can /startserver and /stopserver for you')

@bot.message_handler(commands=['help']) # help message handler
def send_welcome(message):
    bot.reply_to(message, 'You aksed for help..!! I can help you with /startserver and /stopserver')

def checkstatus():
    STATUS_URL = os.getenv('STATUS_URL')
    url = STATUS_URL
    s = requests.get(url)
    s = s.json()
    return s['statuses'][1]['displayStatus']

@bot.message_handler(commands=['startserver']) # help message handler
def send_welcome(message):
    if message.from_user.username in authorized_users:
        status = checkstatus()
        print(status)
        if status != "VM running" and status!= 'VM starting':
            chatid = message.chat.id
            bot.send_message(chatid , "Please wait until we start the server for you..")
            START_URL = os.getenv('START_URL')
            x = requests.get(START_URL).json()
            if x['action_completed'] == "start":
                bot.reply_to(message , 'The server has been started for you, Happy Gaming')
                print(message.from_user.username + " has started the server")
            else:
                bot.reply_to(message , 'Some error occured in starting the server... Please try again')
        else:
            bot.reply_to(message , 'Server is already Up')
    else:
        bot.reply_to(message , 'You are not Authorized to Start the server... ')


@bot.message_handler(commands=['stopserver']) # help message handler
def send_welcome(message):
    if message.from_user.username in authorized_users:
        status = checkstatus()
        print(status)
        if status != "VM stopped" and status!= "VM deallocated" and status!= 'VM deallocating':
            chatid = message.chat.id
            bot.send_message(chatid , "Please wait until we Stop the server for you..")
            STOP_URL = os.getenv('STOP_URL')
            x = requests.get(STOP_URL).json()
            
            if x['action_completed'] == 'powerOff':
                bot.reply_to(message , "SERVER STOPPED.. Hope you enjoyed your game..!!")
                print(message.from_user.username + " has shut down the server")
            else:
                bot.reply_to(message , 'Some error occured in powering off the server... Please try again')
        else:
            bot.reply_to(message , 'Server is already off')
    else:
        bot.reply_to(message , 'You are not Authorized to Stop the server... ')

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!",200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://boiling-castle-52185.herokuapp.com/" + TOKEN)
    return "!",200

if __name__ == "__main__":
    server.run(host="0.0.0.0" , port=int(os.environ.get('PORT' , 5000)))