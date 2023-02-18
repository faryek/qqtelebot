import telebot
import os
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Добро пожаловать в Антейку')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "Переверни меня":
        bot.send_message(message.from_user.id, message.text[::-1])


bot.infinity_polling()