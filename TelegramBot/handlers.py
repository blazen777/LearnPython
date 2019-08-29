import logging
from glob import glob
from random import choice

from utils import get_keyboard, get_user_data

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

def get_contact(bot,update,user_data):
    print(update.message.contact)
    update.message.reply_text(f'Sanks{get_user_data(user_data)}', reply_markup=get_keyboard())

def get_location(bot, update, user_data):
    pass