import telebot
import os
from dotenv import load_dotenv
import requests
from deep_translator import GoogleTranslator

load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

info = bot.get_updates()
print(info)

flag1 = False


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Добро пожаловать в Антейку. Список моих команд доступен по команде /help.')

@bot.message_handler(commands=['ten'])
def set_translate(message):
    global flag1
    flag1 = True
    bot.reply_to(message, 'Перевожу ваши сообщения на английский язык. Для прекращения перевода используйте - /stopt.')

@bot.message_handler(commands=['stopt'])
def stop_translate(message):
    global flag1
    flag1 = False
    bot.reply_to(message, 'Перевод отключён.')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, '''Список моих команд:
/start - Приветствие
/help - Помощь
/ten - Перевод ваших сообщений на английский язык
/stopt - Отключает перевод сообщений''')

@bot.message_handler(commands=['pic'])
def send_pic(message):
    bot.send_photo(message.chat.id, 'https://i.ytimg.com/vi/XGL_rWpBHzE/maxresdefault.jpg')




@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.chat.type == 'supergroup':
        if flag1:
            bot.reply_to(message, GoogleTranslator(source='auto', target='en').translate(message.text))
        elif message.text == "@QqBig_bot Привет":
            bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?")
        elif message.text == "@QqBig_bot Переверни меня":
            bot.send_message(message.chat.id, message.text[:-len(message.text)+len('QqBig_bot'):-1])
        elif message.text == "@QqBig_bot Скок паркуришь?":
            bot.send_message(message.chat.id, 'А ты кто такой собственно, чтобы спрашивать?')
            
    elif message.chat.type == 'private':
        if flag1:
            bot.reply_to(message, GoogleTranslator(source='auto', target='en').translate(message.text))
        elif message.text == "Привет":
            bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?")
        elif message.text == "Переверни меня":
            bot.send_message(message.chat.id, message.text[::-1])
        elif message.text == "Скок паркуришь?":
            bot.send_message(message.chat.id, 'А ты кто такой собственно, чтобы спрашивать?')
        
        
        




bot.infinity_polling()
