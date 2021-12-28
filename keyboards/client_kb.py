from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/Понедельник')
b2 = KeyboardButton('/Темы')
b3 = KeyboardButton('/Галерея')
b4 = KeyboardButton('Поделиться', request_location=True)
b5 = KeyboardButton('Отправить кто я', request_contact=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2, b3).row(b4,b5)