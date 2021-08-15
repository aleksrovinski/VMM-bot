#импорт библиотек
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message
from aiogram.utils import executor
import sqlite3
import emoji
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)


