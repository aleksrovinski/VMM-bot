#импорт библиотек
from typing import Text
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message
from aiogram.utils import executor
import sqlite3
import time
from config import token, pn, vt, sr, ht, pt, admin_id
from prettytable import PrettyTable
import logging
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',

                    level=logging.INFO,

                    )

#proxy_url = 'http://proxy.server:3128'
#bot = Bot(token=token, proxy=proxy_url)
bot = Bot(token=token)
dp = Dispatcher(bot)
dz = 'Думаешь я знаю?!'
dzedit = '0'

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    #joinedFile = open("users.txt","r")
    #joinedUsers = set ()
    #for line in joinedFile:
        #joinedUsers.add(line.strip())
    #if not str(msg.chat.id) in joinedUsers:
        #joinedFile = open("users.txt","a")
        #joinedFile.write(str(msg.chat.id)+ "\n")
        #joinedUsers.add(msg.chat.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    buttons1 = ["Школа", "Обратная связь", "Канал", "Другое", "Другие проекты"] # , "Решение примеров"
    keyboard.add(*buttons1)
    await msg.reply("Привет", reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Школа")
async def school(msg: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Расписание', 'ДЗ', 'Назад']
    keyboard.add(*buttons)
    await msg.reply('Раздел "Школа"', reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "ДЗ")
async def schooldz(msg: types.Message):
    global dz
    await msg.reply(dz)
@dp.message_handler(commands=["dz"])
async def schooldz(msg: types.Message):
    global dz
    await msg.reply(dz)
@dp.message_handler(lambda message: message.text == "Расписание")
async def schoollessons(msg: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="ПН", callback_data='pn'),
        types.InlineKeyboardButton(text="ВТ", callback_data='vt'),
        types.InlineKeyboardButton(text="СР", callback_data='sr'),
        types.InlineKeyboardButton(text="ЧТ", callback_data='ht'),
        types.InlineKeyboardButton(text="ПТ", callback_data='pt'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await msg.reply("Выбери день недели:", reply_markup=keyboard)
@dp.message_handler(commands=["lessons"])
async def schoollessons(msg: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="ПН", callback_data='pn'),
        types.InlineKeyboardButton(text="ВТ", callback_data='vt'),
        types.InlineKeyboardButton(text="СР", callback_data='sr'),
        types.InlineKeyboardButton(text="ЧТ", callback_data='ht'),
        types.InlineKeyboardButton(text="ПТ", callback_data='pt'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await msg.reply("Выбери день недели:", reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Назад")
async def back(msg: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    buttons1 = ["Школа", "Обратная связь", "Канал", "Другое", "Другие проекты"]
    keyboard.add(*buttons1)
    await msg.reply("Главное меню", reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Обратная связь")
async def feedback(msg: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Разработчик", url="t.me/aleksrovi"),
        types.InlineKeyboardButton(text="Github", url="https://github.com/aleksrovinski/VMM-bot/issues"),
        #types.InlineKeyboardButton(text="Прям тут", callback_data="feedback1")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await msg.reply("Выбири вариант обратной связи:", reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Канал")
async def channel(msg: types.Message):
    button = types.InlineKeyboardButton(text="Ссылка", url="t.me/vosmoimemmedia")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)
    await msg.reply("Ссылка:", reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Другое")
async def other(msg: types.Message):
    await msg.reply("Тут пока пусто, из-за миграции на aiogram")
@dp.message_handler(lambda message: message.text == "Другие проекты")
async def otherprojects(msg: types.Message):
    button = types.InlineKeyboardButton(text="Github разработчика", url="https://github.com/aleksrovinski")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)
    await msg.reply("Тут все мои публичные проекты", reply_markup=keyboard)
@dp.callback_query_handler(text="pn")
async def pon(call: types.CallbackQuery):
    await call.message.answer(pn)
@dp.callback_query_handler(text="vt")
async def vto(call: types.CallbackQuery):
    await call.message.answer(vt)
@dp.callback_query_handler(text="sr")
async def sre(call: types.CallbackQuery):
    await call.message.answer(sr)
@dp.callback_query_handler(text="ht")
async def het(call: types.CallbackQuery):
    await call.message.answer(ht)
@dp.callback_query_handler(text="pt")
async def pti(call: types.CallbackQuery):
    await call.message.answer(pt)
@dp.callback_query_handler(text="dzedit", user_id=int(admin_id))
async def dzedit(call: types.CallbackQuery):
    global dzedit
    button = types.InlineKeyboardButton(text='Отмена', callback_data='cancel')
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)
    await call.message.answer('Введите новое ДЗ или нажмите отмена', reply_markup=keyboard)
    dzedit = '1'
@dp.callback_query_handler(text="poweroff", user_id=int(admin_id))
async def poweroff(call: types.CallbackQuery):
    await call.message.answer("Завершаю работу")
    quit()
@dp.callback_query_handler(text="cancel", user_id=int(admin_id))
async def cancel(call: types.CallbackQuery):
    await call.message.answer("На нет и суда нет")
    global dzedit
    dzedit = '0'
@dp.message_handler(commands=['admin'], user_id=int(admin_id))
async def admin(msg: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Выключить", callback_data='poweroff'),
        types.InlineKeyboardButton(text="Изменить ДЗ", callback_data='dzedit')
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await msg.reply("Что бы вы хотели сделать мой господин?", reply_markup=keyboard)
    pass
@dp.message_handler(user_id=int(admin_id))
async def qwerty(msg: types.Message):
    global dz
    global dzedit
    if dzedit == '1':
        dz = msg.text
        dzedit = '0'
        await msg.reply('Отлично дз имененно на: ' + dz)
if __name__ == '__main__':
    executor.start_polling(dp)
