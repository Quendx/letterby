from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
from main import dp
from sqlite import add, buy
kb = ReplyKeyboardMarkup()
kb = ReplyKeyboardMarkup()
kb2 = ReplyKeyboardMarkup()
b1=KeyboardButton('/Продолжить')
b2=KeyboardButton('/Остановить')
b3=KeyboardButton('/Непротив')
b4=KeyboardButton('/Против')
kb.add(b1).add(b2)
kb2.add(b3).add(b4)

async def on_startup(_):
    print("bot is online")

@dp.message_handler(commands=['start'])
async def strt(message: types.Message):
    await message.answer(text="Привет! Если ты запустила этот бот, значит, моя валентинка дошла до тебя.",
                         reply_markup=kb)
@dp.message_handler(commands=['Продолжить'])
async def contin(message: types.Message):
    await message.answer(text="Я видел тебя в универе и очень хотел бы познакомиться с тобой по ближе. Не против ли ты ?",reply_markup=kb2)
@dp.message_handler(commands=['Непротив'])
async def ans(message: types.Message):
    await message.answer(text="Меня зовут Маргулан,я с группы Cs-2122      "
                              "Оставь ссылку на телеграм         "
                              "Пример: /add @Quend_x")
@dp.message_handler(commands=['Против'])
async def prosto(message: types.Message):
    await message.answer(text=" ")
@dp.message_handler(commands=['Остановить'])
async def stop(message: types.Message):
    await message.answer(text=" ")
@dp.message_handler(Command('add'))
async def add_cmd(message: Message):
    s = ' '.join(message.text.split(' ')[1:])
    await add(s)
    await message.answer('Успешно добавлено!!!')

@dp.message_handler(Command('buy'))
async def buy_cmd(message: Message):
    await message.answer(await buy())