import telebot
from telebot import types
import config
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/start")
    btn2 = types.KeyboardButton("/help")
    btn3 = types.KeyboardButton("/status")
    markup.add(btn1,btn2)
    bot.send_message(message.chat.id,text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if (message.text == "/help"):
        bot.send_message(message.chat.id, text="Здесь будут указаны авторы: ", reply_markup=markup)
        
    elif (message.text == "/status"):
        bot.send_message(message.chat.id, text="Статус: ")



bot.polling(none_stop=True)