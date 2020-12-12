# -*- coding: utf-8 -*-
__author__ = 'roman'
import telebot
from time import sleep
import sqlite3 as lite
import random
from telebot import *
import datetime
# токен от бота
token = 'token'
bot = telebot.TeleBot(token)
def add_friend(user_id):
    conn = lite.connect('users.sqlite3')
    with conn:
        cur = conn.cursor()
        cur.execute('update users set invite = invite + 1 where  user=%s'%(user_id))
        cur.execute('update users set balance = balance + 30 where  user=%s'%(user_id))
def add_score(user_id):
    conn = lite.connect('users.sqlite3')
    with conn:
        cur = conn.cursor()
        cur.execute('update users set score = score + 1 where  user=%s'%(user_id))
        cur.execute('update users set balance = balance + 10 where  user=%s'%(user_id))
def capcha_check(message, cap):
    if message.text == '◀️ Главное меню':
       glavnoe_menu(message)
    elif message.text == cap:
        user_id = str(message.from_user.id)
        add_score(user_id)
        bot.send_message(message.chat.id, 'Молодец!')
        zarab(message)
    elif message.text != cap:
        bot.send_message(message.chat.id, 'Неправильно!')
        zarab(message)
@bot.message_handler(commands=['ref'])
def welcome_ref_msg(message):
    splited = message.text.split()
    if splited[1]:
        add_friend(splited[1])
    else:
        pass
@bot.message_handler(commands=['start'])
def welcome_msg(message):
    try:
        splited = message.text.split()
        print(splited)
        add_friend(splited[1])
    except:
        pass
    user_id = str(message.from_user.id)
    try:
        conn = lite.connect('users.sqlite3')
        with conn:
            cursor = conn.cursor()
            cursor.execute('insert into users values (?,?,?,?)',(user_id,0,0,0))#user text, score int, balance int, invite int
    except:
        pass
    markup = types.ReplyKeyboardMarkup(True)#разрешаем экранную клавиатуру
    markup.row('👨🏻‍💻Начать зарабатывать')#создаем кнопки
    markup.row('👤Профиль','📊Статистика')
    markup.row('💳Вывести','💼Партнерам')
    markup.row('💰Больше денег')
    bot.send_message(message.chat.id, 'Выберите пункт меню 👇', reply_markup=markup)
@bot.message_handler(regexp=('◀️ Главное меню'))
def glavnoe_menu(message):
    markup = types.ReplyKeyboardMarkup(True)#разрешаем экранную клавиатуру
    markup.row('👨🏻‍💻Начать зарабатывать')#создаем кнопки
    markup.row('👤Профиль','📊Статистика')
    markup.row('💳Вывести','💼Партнерам')
    markup.row('💰Больше денег')
    bot.send_message(message.chat.id, 'Выберите пункт меню 👇', reply_markup=markup)
@bot.message_handler(regexp=('👨🏻‍💻Начать зарабатывать'))
def zarab(message):
    markup = types.ReplyKeyboardMarkup(True)
    markup.row('◀️ Главное меню')
    bot.send_message(message.chat.id, 'Введи капчу!', reply_markup=markup)
    filename = random.choice(os.listdir("samples/"))
    captchaimg = open('samples/'+filename, 'rb')
    bot.send_photo(message.chat.id, captchaimg)
    cap = filename[:5]
    bot.register_next_step_handler(message, capcha_check, cap)
@bot.message_handler(regexp=('👤Профиль'))
def profile(message):
    name = str(message.from_user.first_name)
    username = str(message.from_user.username)
    user_id = str(message.from_user.id)
    conn = lite.connect('users.sqlite3')
    with conn:
        cursor = conn.cursor()
        cursor.execute('select * from users where user=%s'%(user_id))
        row = cursor.fetchone()
    score = str(row[1])
    balance = str(row[2])
    friends = str(row[3])
    bot.send_message(message.chat.id, '👤Мой профиль:\n\nИмя: '+name+'\n Username: '+username+'\n Баланс: '+balance+' р.\n Просмотрено капч: '+score+'\n Приглашено:'+friends)

@bot.message_handler(regexp=('💳Вывести'))
def vivod(message):
    markup = types.ReplyKeyboardMarkup(True)#разрешаем экранную клавиатуру
    markup.row('👨🏻‍💻Начать зарабатывать')#создаем кнопки
    markup.row('👤Профиль','📱Телефон')
    bot.send_message(message.chat.id, markup)
    return

@bot.message_handler(regexp=('💼Партнерам'))
def partneram(message):
    user_id = str(message.from_user.id)
    bot.send_message(message.chat.id, 'Получи бонус 20р за каждого приглашенного друга по ссылке:  https://t.me/Testoviymusbot?start=%s'%(user_id))
    return

@bot.message_handler(regexp=('💰Больше денег'))
def bolshedeneg(message):
    markup = types.InlineKeyboardMarkup()#разрешаем кнопки в сообщениях
    ref = types.InlineKeyboardButton(text='Перейти на канал', url='t.me/reflink1337')#создаем конпки в сообщениях
    markup.add(ref)
    bot.send_message(message.chat.id, "Хочешь больше денег? \n Чтобы заработать дополнительно 400 рублей, просто подпишитесь на канал партнеров и просмотрите ближайшие 15 постов!", reply_markup = markup)
@bot.message_handler(regexp=('7Назад'))
def nazad(message):
    markup = types.ReplyKeyboardMarkup(True)
    markup.row('👨🏻‍💻Начать зарабатывать')
    markup.row('👤Профиль')
    markup.row('💳Вывести','💼Партнерам')
    markup.row('6Больше денег')
    bot.send_message(message.chat.id, 'Выберите пункт меню 👇', reply_markup=markup)
def glavnoeMenu(message):
    markup = types.ReplyKeyboardMarkup(True)
    markup.row('👨🏻‍💻Начать зарабатывать')
    markup.row('👤Профиль')
    markup.row('💳Вывести','💼Партнерам')
    markup.row('💰Больше денег')
    bot.send_message(message.chat.id, 'Вы вернулись в главное меню', reply_markup=markup)
try:
    while True:
        bot.polling()
except Exception as l:
    error = str(l)
    tday = str(datetime.date.today())
    with open('log.txt', 'a') as log:
        log.write(tday+' : '+error+'\n')
    sleep(3)

