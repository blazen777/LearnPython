CatBot
======

CatBot - это бот для Telegram сделанный с целью делать вашу жизнь, лучше присылая вам котиков.

Установка:
----------

Создайте виртуальное окружение и активируйте его.
Потом в виртуальном окружении выполните:

.. code-block:: text

    pip install -r requirements.txt

Положите картинки с котиками в папку img.
Название файлов должно начинаться с cat, а расширение jpg

Настройка:
----------

Создайте свой файл setting.py и добавьте туда следующие найстройки:

.. code-block:: python

    token = "token-ключ который вы получили у BotFather"

    user_emoji = [':smiley_cat:', ':+1:', ':smiling_imp:', ':panda_face:', ':dog:', ':boy:'] 