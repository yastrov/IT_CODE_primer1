import telebot
import os

bot = telebot.TeleBot('5540455192:AAFPTvwJkiVEja42IMKw4U2Qzs8_amm_9Bw')

from telebot import types

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_work = types.KeyboardButton('Шутки')
    btn_help = types.KeyboardButton('Помощь')
    markup.add(btn_work, btn_help)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_info(message):
    if message.text == "Шутки":
        markup_inline = types.InlineKeyboardMarkup(row_width=2)
        cours1 = types.InlineKeyboardButton('Про бабушку', callback_data='cour1')
        cours2 = types.InlineKeyboardButton('Про Стал', callback_data='cour2')
        markup_inline.add(cours1,cours2)
        bot.send_message(message.chat.id, 'Выбери что-то', reply_markup=markup_inline)
    elif message.text == "Помощь":
        bot.send_message(message.chat.id, 'Тебе никто не поможет')
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю!")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'cour2':
        bot.send_message(call.message.chat.id, 'У старой бабушки кошка родила двух котят. И чтобы не забыть имена котят, бабушка первого котенка назвала Барсик, а второго утопила')
    elif call.data == 'cour1':
        bot.send_message(call.message.chat.id, 'Стал разъезжал на двух танках по очереди. Толпа возмущалась, но не расходилась.')

bot.polling(none_stop=True,interval=0)

