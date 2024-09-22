from aiogram import Bot, Dispatcher
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from constants import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

cat_link: str
offset = -2

# Creating button objects
button_1 = KeyboardButton(text='Хочу котика (не 🦮)')
button_2 = KeyboardButton(text='я огурец 🥒')

# Create a keyboard object by adding buttons to it
keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]])