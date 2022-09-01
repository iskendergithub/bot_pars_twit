import telebot
from telebot import types
from pars import Parser

bot = telebot.TeleBot("5647356669:AAG_busl0IEYR7NXddsy1TDwrjGRBAVHCxc")


@bot.message_handler(commands=["start"])
def hello(user):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button3 = types.InlineKeyboardButton('Найти ссылки на все курсы!)', callback_data='check_lessons')
    button1 = types.InlineKeyboardButton('Принять блоки курса!', callback_data='check_blocks')

    markup.add(button3, button1)
    bot.send_message(user.chat.id, text="Добро пожаловать в бот,"
                                        " находящий курсы и их блоки! "
                     , reply_markup=markup)


@bot.callback_query_handler(func=lambda c: c.data == 'check_lessons')
def show_lessons(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    f = open('urls_to_learn', 'r', encoding='utf-8')
    text = f.read()
    bot.send_message(callback_query.from_user.id, text)


@bot.callback_query_handler(func=lambda c: c.data == 'check_blocks')
def select_int(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    text = 'Выберите номер курса!(1, 2, 3, 4, 5, 6)'
    bot.send_message(callback_query.message.chat.id, text)


@bot.message_handler(content_types=['text'])
def show_blocks(message):
    c = Parser()
    a = message.text
    b = c.urls_and_check(int(a))
    bot.send_message(message.chat.id, text='\n'.join(b))


bot.infinity_polling()
