# import telebot
# from telebot import types  # для указание типов
#
#
# bot = telebot.TeleBot('7175004949:AAHSNKcUe42Nsw5cTEzIbzLpzU6Rq_70wPE)
#
#
# # Добавляем декораторы
# @bot.message_handler(commands=['start'])
# # Хранит информацию про самого пользователя и чат
# def main(message):
#     # бот отвечает на команду
#     bot.send_message(message.chat.id, f'Привет{message.from_user.first_name} {message.from_user.last_name}')
#
# #
# # @bot.message_handler(commands=['site','wibesite'])
# # def site(message):
# #     return webbrowser.open('http://192.168.0.167:5000')
# @bot.message_handler(commands=['site'])
# def site(message):
#     markup = types.InlineKeyboardMarkup()  # создаём кнопку
#     button1 = types.InlineKeyboardButton("Нажми", url='http://192.168.0.167:5000')  # добавляем текст кнопки и ссылку
#     markup.add(button1)  # добавляем кнопку
#     bot.send_message(message.chat.id, "ссылка на веб сайт",
#                      reply_markup=markup)  # отправляем сообщение со встроенной кнопкой
# bot.polling(none_stop=True)  # Работа бота не прекращалась

import telebot
import webbrowser

TOKEN = '7175004949:AAHSNKcUe42Nsw5cTEzIbzLpzU6Rq_70wPE'

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def main(message):
    # бот отвечает на команду
    bot.send_message(message.chat.id, f'Привет{message.from_user.first_name} {message.from_user.last_name}')
@bot.message_handler(commands=['site'])
def open_site(message):
    chat_id = message.chat.id
    site_url = 'http://127.0.0.1:5000'
    bot.send_message(chat_id, f"Открываю сайт {site_url}")
    webbrowser.open(site_url)

bot.polling()


