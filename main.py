from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove

import sqlite

from config import BOT_TOKEN



bot=Bot(BOT_TOKEN)
dp=Dispatcher(bot)

kb = ReplyKeyboardMarkup()
kb2 = ReplyKeyboardMarkup()
b1=KeyboardButton('/Продолжить')
b2=KeyboardButton('/Остановить')
b3=KeyboardButton('/Непротив')
b4=KeyboardButton('/Против')
kb.add(b1).add(b2)
kb2.add(b3).add(b4)








if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)