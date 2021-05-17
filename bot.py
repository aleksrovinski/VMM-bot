import pyttsx3 #импорт синтеза речи
from gtts import gTTS #импорт синтеза речи
import datetime #модуль времени
import telebot # модуль для работы с api telegram
from telebot import types
soszaloba = '0' #состояние жалобы
id =  #здесь id админа
now = datetime.date.today()
update = datetime.date(2021,5,15)
print(now) #вывод текущей даты
print(update) #вывод даты обновления дз
dz1 = '***' #переменная с домашкой
TOKEN = 'YOUR TOKEN' #токен бота
bot = telebot.TeleBot(TOKEN)
tts = gTTS(dz1)
tts.save('dz1.mp3')
if update != now:
    bot.send_message(id, 'Обнови дз') #уведомление для админа
	
@bot.message_handler(commands=['start'])
def welcome(message):
    # клавиатура тг
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Жалоба")
    item2 = types.KeyboardButton("Я хочу поговорить.")
    item3 = types.KeyboardButton("Расписание")
    item4 = types.KeyboardButton("Домашнее задание")

    markup.add(item3, item4, item2, item1)
    #приветственное сообщение
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный @aleksrovinski .".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    if update != now:
            #уведомление для админа
            bot.send_message(id, 'Обнови дз')

@bot.message_handler(content_types=['text'])
def lalala(message):
    global soszaloba
    #if message.chat.type == 'private': (примеч. данная строчка отвечает за работу бота в группах)
    if message.text == 'Расписание':
        #Реакция на текст 'Рассписание'
        markup1 = types.InlineKeyboardMarkup(row_width=8)
        item1 = types.InlineKeyboardButton('ПН', callback_data='pn')
        item2 = types.InlineKeyboardButton('ВТ', callback_data='vt')
        item3 = types.InlineKeyboardButton('СР', callback_data='sr')
        item4 = types.InlineKeyboardButton('ЧТ', callback_data='ht')
        item5 = types.InlineKeyboardButton('ПТ', callback_data='pt')

        markup1.add(item1, item2, item3, item4, item5)


        bot.send_message(message.chat.id, 'Выбери день:', reply_markup=markup1)
        if update != now:
            #уведомление для админа
            bot.send_message(id, 'Обнови дз')
    elif message.text == "Я хочу поговорить.":
        #Реакция на текст "Я хочу поговорить."
        bot.send_message(message.chat.id, 'К сожалению я не умею нормально говорить, но у меня есть знакомый @chat7mbot он может с тобой поговорить.')
        if update != now:
            #уведомление для админа
            bot.send_message(id, 'Обнови дз')    
    elif message.text == "Жалоба":
        #Реакция на текст "Жалоба"
        markup2 = types.InlineKeyboardMarkup(row_width=8)
        item2 = types.InlineKeyboardButton('Второй', callback_data='2')
        markup2.add(item2)
        bot.send_message(message.chat.id, "В данном случае есть два варианта. Первый(наиболее надёжный вариант) - напиши @aleksrovi. Второй - заполнить анкету которая будет переслана @aleksrovi.", reply_markup=markup2)
        soszaloba = '1'

    elif message.text == 'Домашнее задание':
        #Реакция на текст "Домашнее задание"
        bot.send_message(message.chat.id, dz1 )
        audio = open(r'путь/до/папки/с/файлом/dz1.mp3', 'rb')
        bot.send_chat_action(message.chat.id, 'upload_audio')
        bot.send_audio(message.chat.id, audio)
        audio.close()
        if update != now:
            #уведомление для админа
            bot.send_message(id, 'Обнови дз')


    else:
        
        print(soszaloba)
        if soszaloba == '1':
            #работа с жалобой
            zaloba = message.text
            bot.send_message(id, zaloba)
            bot.send_message(message.chat.id, 'Жалоба отправлена, спасибо за обратную связь.')
            soszaloba = '0'
        elif soszaloba == '0':
            #в случае если сообщание не имеет смысла
            bot.send_message(message.chat.id, 'Я не знаю что ответить')
            

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global soszaloba
    try:
        if call.message:
            #Рассписание
            if call.data == 'pn':
                bot.send_message(call.message.chat.id, '<b>Расписание на Понедельник:</b> \n1.Русский язык. \n2.Обществознание. \n3.Алгебра. \n4.Геометрия. \n5.История России. \n6.Английский язык. \n<b>Дополнительные:</b> \n7.Физика, \n8.Математика.', parse_mode="html")
            elif call.data == 'vt':
                bot.send_message(call.message.chat.id, '<b>Расписание на Вторник:</b> \n1.Алгебра. \n2.Физика. \n3.Технология. \n4.Технология. \n5.Физическая культура. \n6.Статистика и теория вероятностей. \n<b>Дополнительные:</b> \nНЕТ', parse_mode="html")
            elif call.data == 'sr':
                bot.send_message(call.message.chat.id, '<b>Расписание на Среду:</b> \n1.Русский язык. \n2.Биология. \n3.Алгебра. \n4.Литература. \n5.Английский язык. \n6.Геометрия. \n7.Физика. <b>Дополнительные:</b> НЕТ', parse_mode="html")
            elif call.data == 'ht':
                bot.send_message(call.message.chat.id, '<b>Расписание на Четверг:</b> \n1.Литература. \n2.Физичекая культура. \n3.Русский язык. \n4.Английский язык. \n5.География. \n6.Алгебра. \n<b>Дополнительные:</b> \n7.Классный час(чаще всего обязателен).', parse_mode="html")
            elif call.data == 'pt':
                bot.send_message(call.message.chat.id, "<b>Расписанние на Пятницу:</b> \n1.Алгебра. \n2.Геометрия. \n3.Биология. \n4.История России. \n5.География. \n6.Информатика. \n7.Русский язык. \n<b>Дополнительные:</b> \n8.Математика. \n9.Английский язык(2 группа).", parse_mode="html")
            elif call.data == '2':
                #жалоба
                soszaloba = '1'
                markup3 = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Отмена", callback_data='cancel')
                markup3.add(item1)
                bot.send_message(call.message.chat.id, 'Напишите в чём заключается ваше недовольство.', reply_markup=markup3)
                bot.send_message(994433789,'Начато составление жалобы')
                soszaloba = '1'
                print(soszaloba)
                if update != now:
                    #уведомление для админа
                    bot.send_message(id, 'Обнови дз')    
            elif call.data == 'cancel':
                #отмена жалобы
                bot.send_message(id,'Галя отмена.')
                bot.send_message(call.message.chat.id, 'На нет и суда нет')
                soszaloba = '0'
                print(soszaloba)


            #сообщение пользователю по завершению всего выше перечисленного
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Выполнено")

    except Exception as e:
        print(repr(e))






#беспрерывная работа
bot.polling()
