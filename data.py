# file with data



import requests
from aiogram import Bot, Dispatcher
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from constants import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

cat_response: requests.Response
cat_link: str
offset = -2

# Создаем объекты кнопок
button_1 = KeyboardButton(text='Хочу котика (не 🦮)')
button_2 = KeyboardButton(text='я огурец 🥒')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]])