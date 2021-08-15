#импорт библиотек
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message
from aiogram.utils import executor
import sqlite3
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons1 = ["Школа", "Обратная связь", "Канал", "Другое", "Другие проекты"]
    keyboard.add(*buttons1)
    await message.reply("Привет", reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)