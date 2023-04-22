# Здесь должна находиться основная логика программы. by Sihionok.
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    btn2 = types.KeyboardButton("Выбрать сайт")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)





bot.polling(none_stop=True)