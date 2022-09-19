import telebot
from telebot import types

bot = telebot.TeleBot('5678954519:AAElMtIRw-8dYFG56-d49wwSxZari1uLaHg')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')

    question(message)


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hello':
#         mess = 'И тебе привет!'
#         bot.send_message(message.chat.id, mess, parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('photo.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, 'Я не понял :(', parse_mode='html')


# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, 'Крутая фотка!', parse_mode='html')


# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Посетить вэбсайт', url='https://google.com'))
#     bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def question(message):
    mess = 'Нормально'
    if message.text in ('Помощь', '/start'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=False)

        study = types.KeyboardButton('Как дела с учёбой?')
        work = types.KeyboardButton('Как дела на работе?')

        markup.add(study, work)
        bot.send_message(message.chat.id, 'Выбери интересующий тебя вопрос:', reply_markup=markup)
    elif message.text == 'Как дела с учёбой?':
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == 'Как дела на работе?':
        bot.send_message(message.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True)
