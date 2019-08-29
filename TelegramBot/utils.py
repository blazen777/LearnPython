from random import choice

from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton


from settings import user_emoji


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