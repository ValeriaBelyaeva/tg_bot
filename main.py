from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message

from data import keyboard, bot, dp
from functions import *

if __name__ == '__main__':
    dp.run_polling(bot)