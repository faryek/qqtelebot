import telebot
import os
from dotenv import load_dotenv
import requests
from deep_translator import GoogleTranslator
import requests
from bs4 import BeautifulSoup as bs
import random



def pikabu_post(query):
    result = []
    if query != 'None' and query != 'QqBig_bot':
        url = 'https://pikabu.ru/search?q='+query+'&st=3'
    else:
        url = 'https://pikabu.ru/new'
    page = requests.get(url)
    exbs = bs(page.text, 'lxml')
    temp = exbs.find_all('a', class_='story__title-link')
    ind = random.randrange(0,len(temp))
    url2 = temp[ind].get('href')
    page2 = requests.get(url2)
    newbs = bs(page2.text, 'lxml')
    title = newbs.find('span', class_='story__title-link')
    title = title.get_text()
    result.append(title+'\n\n'+'Ссылка на пост: '+url2)
    return result

load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

info = bot.get_updates()
print(info)

flag1 = False
tg = 'en'
id_fortl = 0


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Добро пожаловать в Антейку. Список моих команд доступен по команде /help.')

@bot.message_handler(commands=['to'])
def set_translate(message):
    global flag1
    global tg
    global id_fortl
    flag1 = True
    id_fortl = message.from_user.id
    if message.text[4::] == 'english' or message.text[4::] == 'en' or message.text[4::] == 'английский':
        bot.reply_to(message, 'Перевожу ваши сообщения на английский язык. Для прекращения перевода используйте - /stopt.')
        tg = 'en'
    elif message.text[4::] == 'ukrainian' or message.text[4::] == 'uk' or message.text[4::] == 'украинский':
        bot.reply_to(message, 'Перевожу ваши сообщения на украинский язык. Для прекращения перевода используйте - /stopt.')
        tg = 'uk'
    elif message.text[4::] == 'chinese' or message.text[4::] == 'zh' or message.text[4::] == 'китайский':
        bot.reply_to(message, 'Перевожу ваши сообщения на китайский язык. Для прекращения перевода используйте - /stopt.')
        tg = 'zh-CN'
    elif message.text[4::] == 'japanese' or message.text[4::] == 'ja' or message.text[4::] == 'японский':
        bot.reply_to(message, 'Перевожу ваши сообщения на японский язык. Для прекращения перевода используйте - /stopt.')
        tg = 'ja'
    elif message.text[4::] == 'german' or message.text[4::] == 'de' or message.text[4::] == 'немецкий':
        bot.reply_to(message, 'Перевожу ваши сообщения на немецкий язык. Для прекращения перевода используйте - /stopt.')
        tg = 'de'
    elif message.text[4::] == 'russian' or message.text[4::] == 'ru' or message.text[4::] == 'русский':
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
/pic - Прикольная картинка
/pika [Тема поста] - Случайный свежий пост с Пикабу на нужную тему, если она указана''')

@bot.message_handler(commands=['pic'])
def send_pic(message):
    bot.send_photo(message.chat.id, 'https://i.ytimg.com/vi/XGL_rWpBHzE/maxresdefault.jpg')

@bot.message_handler(commands=['pika'])
def send_post(message):
    post = pikabu_post(message.text[6::])
    if len(post) == 1:
        bot.send_message(message.chat.id, post[0])



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global tg
    if message.chat.type == 'supergroup':
        if flag1 and message.from_user.id == id_fortl:
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
