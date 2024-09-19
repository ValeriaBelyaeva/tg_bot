from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup)
from constants import *
import requests

from data import keyboard, bot, dp

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Чего ты хочешь?',
        reply_markup=keyboard
    )

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Чего ты хочешь?',
        reply_markup=keyboard
    )

@dp.message(F.text == 'Хочу котика (не 🦮)')
async def process_dog_answer(message: Message):
    await message.answer(
        text='Держи котика:'
    )
    cat_response = requests.get(API_CATS_URL)
    cat_link = cat_response.json()[0]['url']
    print(cat_link)
    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={message.chat.id}&photo={cat_link}')

@dp.message(F.text == 'я огурец 🥒')
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='тебе виднее. Но лучше подпишись на t.me/ITMO_stud'
    )
@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        # await message.send_copy(chat_id=message.chat.id)
        await message.reply("Мне приятно, что ты хочешь со мной поболтать, но я умею только отсылать котиков")
        print(message.chat.full_name, "sending '", message.text, "'")
    except TypeError:
        await message.answer("Ваше сообщение ломает бота(")