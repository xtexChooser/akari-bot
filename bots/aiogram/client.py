from aiogram import Bot, Dispatcher

from config import Config

token = Config('tg_token')

if token:
    bot = Bot(token=token)
    dp = Dispatcher(bot)
else:
    bot = dp = False
