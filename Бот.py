import telebot
from telebot.types import Message
import random

TOKEN = '799797686:AAEuo8gxij06Uz2Kfukxjyziykum5yRORqg'
bot = telebot.TeleBot(TOKEN)
stickers = [
    '😂',
    '😘',
    '❤',
    '😊',
    '😁',
    '☺',
    '😄',
    '😭',
    '💋',
    '😒',
    '😡',
    '🙊',
    '😐',
    '😕',
    '😌',
    '😋',
    '😀',
    '🥶'
]

#bot.send_message(531184087,'Стелла, привет!!!!!1') #Вывод спантанного сообщения
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    name = message.from_user.first_name  # Берем имя пользователя
    if message.chat.id==531184087:
        bot.send_message(message.chat.id, 'Привет, ' + name )  # Вывод
    else:
        bot.send_message(message.chat.id, 'Вали отсюда ' + name )  # Вывод


@bot.message_handler(content_types=['text'])
def UPPER(message):
    bot.reply_to(message, random.choice(stickers))
    # bot.send_message(message.chat.id, message.text.upper())


bot.polling(none_stop=True)
