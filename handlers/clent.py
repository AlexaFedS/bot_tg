from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

#@dp.message_handler(commands=['start','help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Welcome', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через личные сообщения, напишите ему:\nBKIT_DZ_telegram_bot')

#@dp.message_handler(commands=['Понедельник'])
async def pon_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'День тяжелый... Работаем!')

#@dp.message_handler(commands=['Темы'])
async def theme_open_command(message:types.Message):
    await bot.send_message(message.from_user.id, 'ховерборд')

async def pict_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pon_open_command, commands=['Понедельник'])
    dp.register_message_handler(theme_open_command, commands=['Темы'])
    dp.register_message_handler(pict_menu_command, commands=['Галерея'])
