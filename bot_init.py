import configparser
from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage

config = configparser.ConfigParser()

def bot_init():
    config.read("./settings/config.ini")
    token = config['BOT']['token']
    bot_name = config['BOT']['bot_name']
    bot = Bot(token=token)
    dp = Dispatcher(storage=MemoryStorage())
    router = Router()
    dp.include_router(router)
    return bot, dp, router, bot_name


