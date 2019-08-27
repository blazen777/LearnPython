from glob import glob
import logging
from random import choice

from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler,RegexHandler, Filters

from settings import token, user_emoji


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)

def greeting(bot, update, user_data):
    emoji = get_user_data(user_data)
    msg = f"Hello, {emoji}"
    
    update.message.reply_text(msg,reply_markup=get_keyboard())

def talk_to_me(bot, update, user_data):
    # Ответ от бота
    get_user_data(user_data)
    user_msg = f"Привет {update.message.chat.first_name} {user_data['emoji']}!! \nТы написал: {update.message.text}"
    logging.info(f'User: {update.message.chat.username}, Chat id: {update.message.chat.id}, Message: {update.message.text}')
    update.message.reply_text(user_msg, reply_markup=get_keyboard())

def send_cat_img(bot, update, user_data):
    """ Посылает картинку с котом из папки img, при вводе команды /cat"""
    cat_list = glob('img/cat*.jpg')
    cat_img = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_img, 'rb'), reply_markup=get_keyboard())

def change_emoji(bot, update, user_data):
    if 'emoji' in user_data:
        del user_data['emoji']
    emoji = get_user_data(user_data)
    update.message.reply_text(f'Done. {emoji}', reply_markup=get_keyboard())

def get_user_data(user_data):
    if 'emoji' in user_data:
        return user_data['emoji']
    else:
        user_data['emoji'] = emojize(choice(user_emoji), use_aliases=True)
        return user_data['emoji']

def get_keyboard():
    contact = KeyboardButton('Send contact', request_contact=True)
    location = KeyboardButton('Get geolocation', request_location=True)
    # add keyboard to show cats
    my_keyboard = ReplyKeyboardMarkup([
        ['Доставить котяру', 'Сменить смайлик'],
        [contact, location],
        ], resize_keyboard=True)
    
    return my_keyboard


def get_contact(bot,update,user_data):
    print(update.message.contact)
    update.message.reply_text(f'Sanks{get_user_data(user_data)}', reply_markup=get_keyboard())

def get_location(bot, update, user_data):
    pass

def main():
    bot = Updater(token)

    logging.info('Bot is running')
    # Добавить обработчик
    dp = bot.dispatcher
    # Обработчик комманд
    dp.add_handler(CommandHandler("start", greeting, pass_user_data=True))
    # Ставить все хэндлеры до VessageHandler
    dp.add_handler(CommandHandler("cat", send_cat_img, pass_user_data=True))

    dp.add_handler(RegexHandler('^(Доставить котяру)$', send_cat_img,pass_user_data=True))
    dp.add_handler(RegexHandler('^(Сменить смайлик)$', change_emoji ,pass_user_data=True))

    # Обработчик сообщений
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))
    # начать проверку сообщений
    bot.start_polling()
    # работать до момента остановки
    bot.idle()


main()