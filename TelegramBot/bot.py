from telegram.ext import Updater, CommandHandler, MessageHandler,RegexHandler, Filters

from handlers import *
from settings import token


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)

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


if __name__ == "__main__":
    main()