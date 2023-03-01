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
tg = 'en'


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Добро пожаловать в Антейку. Список моих команд доступен по команде /help.')

@bot.message_handler(commands=['to'])
def set_translate(message):
    global flag1
    global tg
    flag1 = True
    if message.text[4::] == 'english' or message.text[4::] == 'en':
        bot.reply_to(message, 'Перевожу ваши сообщения на английский язык. Для прекращения перевода используйте - /stopt.')
        tg = 'en'
    elif message.text[4::] == 'ukrainian' or message.text[4::] == 'uk':
        bot.reply_to(message, 'Перевожу ваши сообщения на украинский язык. Для прекращения перевода используйте - /stopt.')
        tg = 'uk'
    elif message.text[4::] == 'chinese' or message.text[4::] == 'zh':
        bot.reply_to(message, 'Перевожу ваши сообщения на китайский язык. Для прекращения перевода используйте - /stopt.')
        tg = 'zh'
    elif message.text[4::] == 'japanese' or message.text[4::] == 'ja':
        bot.reply_to(message, 'Перевожу ваши сообщения на японский язык. Для прекращения перевода используйте - /stopt.')
        tg = 'ja'
    elif message.text[4::] == 'german' or message.text[4::] == 'de':
        bot.reply_to(message, 'Перевожу ваши сообщения на немецкий язык. Для прекращения перевода используйте - /stopt.')
        tg = 'de'
    elif message.text[4::] == 'russian' or message.text[4::] == 'ru':
        bot.reply_to(message, 'Перевожу ваши сообщения на русский язык. Для прекращения перевода используйте - /stopt.')
        tg = 'ru'
    else:
        bot.reply_to(message, 'Похоже я не могу переводить на этот язык. :(')

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
/to [язык] - Перевод ваших сообщений на указанный язык.
На данный момент доступны: английский, украинский, китайский, японский, немецкий.
/stopt - Отключает перевод сообщений
/pic - Прикольная картинка''')

@bot.message_handler(commands=['pic'])
def send_pic(message):
    bot.send_photo(message.chat.id, 'https://i.ytimg.com/vi/XGL_rWpBHzE/maxresdefault.jpg')




@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global tg
    if message.chat.type == 'supergroup':
        if flag1:
            bot.reply_to(message, GoogleTranslator(source='auto', target=tg).translate(message.text))
        elif message.text == "@QqBig_bot Привет":
            bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?")
        elif message.text == "@QqBig_bot Переверни меня":
            bot.send_message(message.chat.id, message.text[:-len(message.text)+len('QqBig_bot'):-1])
        elif message.text == "@QqBig_bot Скок паркуришь?":
            bot.send_message(message.chat.id, 'А ты кто такой собственно, чтобы спрашивать?')
        elif message.text == 'xd':
            bot.send_message(message.chat.id, 'xd')
        elif message.text == "@QqBig_bot Какая игра лучшая?":
            bot.send_message(message.chat.id, 'Думаешь тут будет Genshin Impact? НЕТ! Это Persona 5!!!')
            bot.send_photo(message.chat.id, 'https://cdn.vox-cdn.com/thumbor/PyOsRTbkSQRZH1eFj6mzMUvUBD4=/0x0:1437x771/1200x675/filters:focal(1090x283:1318x511)/cdn.vox-cdn.com/uploads/chorus_image/image/64062696/Screen_Shot_2016-09-13_at_1.44.05_PM.0.0.png')
    elif message.chat.type == 'private':
        if flag1:
            bot.reply_to(message, GoogleTranslator(source='auto', target=tg).translate(message.text))
        elif message.text == "Привет":
            bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?")
        elif message.text == "Переверни меня":
            bot.send_message(message.chat.id, message.text[::-1])
        elif message.text == "Скок паркуришь?":
            bot.send_message(message.chat.id, 'А ты кто такой собственно, чтобы спрашивать?')
        elif message.text == "Какая игра лучшая?":
            bot.send_message(message.chat.id, 'Думаешь тут будет Genshin Impact? НЕТ! Это Persona 5!!!')
            bot.send_photo(message.chat.id, 'https://cdn.vox-cdn.com/thumbor/PyOsRTbkSQRZH1eFj6mzMUvUBD4=/0x0:1437x771/1200x675/filters:focal(1090x283:1318x511)/cdn.vox-cdn.com/uploads/chorus_image/image/64062696/Screen_Shot_2016-09-13_at_1.44.05_PM.0.0.png')
        elif message.text == 'xd':
            bot.send_message(message.chat.id, 'xd')
            
        
        




bot.infinity_polling()
