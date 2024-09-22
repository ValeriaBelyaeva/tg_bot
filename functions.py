from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message
from constants import *
import requests

from data import keyboard, dp

# Opening function
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Чего ты хочешь?',
        reply_markup=keyboard
    )

# A function that loads and sends a photo of a cat
def send_kitty(message):
    cat_response = requests.get(API_CATS_URL)
    cat_link = cat_response.json()[0]['url']
    print(cat_link)
    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={message.chat.id}&photo={cat_link}')

# A function that handles a request to click on a function button
@dp.message(F.text == 'Хочу котика (не 🦮)')
async def process_dog_answer(message: Message):
    await message.answer(
        text='Держи котика:'
    )
    send_kitty(message)

# Handling the click event on a decorative button
@dp.message(F.text == 'я огурец 🥒')
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='осторожнее, котики боятся огурцов. Да, лучше смотри их фоточки)'
    )

# Processing sent text messages
@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        # Regular text message
        await message.reply("Мне приятно, что ты хочешь со мной поболтать, но я умею только отсылать котиков")
        print(message.chat.full_name, "sending '", message.text, "'")
    except TypeError:
        # Error Handling
        await message.answer("Ваше сообщение ломает бота(")