#импорт библиотек
from typing import Text
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message
from aiogram.utils import executor
import sqlite3
from config import token, pn, vt, sr, ht, pt
from prettytable import PrettyTable
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    buttons1 = ["Школа", "Обратная связь", "Канал", "Другое", "Другие проекты"]
    keyboard.add(*buttons1)
    await message.reply("Привет", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Школа")
async def school(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Расписание', 'ДЗ', 'Назад']
    keyboard.add(*buttons)
    await message.reply('Раздел "Школа"', reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "ДЗ", commands=['dz'])
async def schooldz(message: types.Message):
    await message.reply("функция отключена до 1.09.2021")
@dp.message_handler(commands=["dz"])
async def schooldz(message: types.Message):
    await message.reply("функция отключена до 1.09.2021")
@dp.message_handler(lambda message: message.text == "Расписание", commands=['lessons'])
async def schoollessons(message: types.Message):
    await message.reply("функция отключена до 1.09.2021")
@dp.message_handler(commands=["lessons"])
async def schoollessons(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="ПН", callback_data='pn'),
        types.InlineKeyboardButton(text="ВТ", callback_data='vt'),
        types.InlineKeyboardButton(text="СР", callback_data='sr'),
        types.InlineKeyboardButton(text="ЧТ", callback_data='ht'),
        types.InlineKeyboardButton(text="ПТ", callback_data='pt'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.reply("функция отключена до 1.09.2021", reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Назад")
async def back(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons1 = ["Школа", "Обратная связь", "Канал", "Другое", "Другие проекты"]
    keyboard.add(*buttons1)
    await message.reply("Главное меню", reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Обратная связь")
async def feedback(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Разработчик", url="t.me/aleksrovi"),
        types.InlineKeyboardButton(text="Github", url="https://github.com/aleksrovinski/VMM-bot/issues"),
        #types.InlineKeyboardButton(text="Прям тут", callback_data="feedback1")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.reply("Выбири вариант обратной связи:", reply_markup=keyboard)
#@dp.callback_query_handler(text="feedback1")
#async def feedbackinbot(call: types.CallbackQuery):
    #buttons = [
        #types.InlineKeyboardButton(text="Отзыв", callback_data="otziv"),
        #types.InlineKeyboardButton(text="Жалоба", callback_data="zaloba"),
        #types.InlineKeyboardButton(text='Что-то не так в разделе "Школа"', callback_data="school")
    #]
    #keyboard = types.InlineKeyboardMarkup(row_width=3)
    #keyboard.add(*buttons)
    #await call.message.answer("Начнём с того что вы хотите отправить:", reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Канал")
async def kanal(message: types.Message):
    button = types.InlineKeyboardButton(text="Ссылка", url="t.me/vosmoimemmedia")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)
    await message.reply("Ссылка:", reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Другое")
async def other(message: types.Message):
    await message.reply("Тут пока пусто, из-за миграции на aiogram")
@dp.message_handler(lambda message: message.text == "Другие проекты")
async def otherprojects(message: types.Message):
    button = types.InlineKeyboardButton(text="Github разработчика", url="https://github.com/aleksrovinski")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)
    await message.reply("Тут все мои публичные проекты", reply_markup=keyboard)
@dp.callback_query_handler(text="pn")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(pn)
@dp.callback_query_handler(text="vt")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(vt)
@dp.callback_query_handler(text="sr")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(sr)
@dp.callback_query_handler(text="ht")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(ht)
@dp.callback_query_handler(text="pt")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(pt)
if __name__ == '__main__':
    executor.start_polling(dp)