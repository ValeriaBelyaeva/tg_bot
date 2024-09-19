from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup)
from constants import *
import requests

# Создаем объекты бота и диспетчера
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
        await message.send_copy(chat_id=message.chat.id)
        print(message.chat.full_name, "sending '", message.text, "'")
    except TypeError:
        await message.answer("Ваше сообщение ломает бота(")
if __name__ == '__main__':
    dp.run_polling(bot)