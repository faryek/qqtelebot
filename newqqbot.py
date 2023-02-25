import telebot
import os
from dotenv import load_dotenv
import requests

load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

info = bot.get_updates()
print(info)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Добро пожаловать в Антейку. Список моих команд доступен по команде /help.')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Антейку')






@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "@QqBig_bot Привет":
        bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "@QqBig_bot Переверни меня":
        bot.send_message(message.chat.id, message.text[::-1])




bot.infinity_polling()
