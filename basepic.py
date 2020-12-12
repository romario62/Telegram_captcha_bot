__author__ = 'roman'

# -*- coding: utf-8 -*-

# Подключаем библиотеки
import sqlite3 as lite
import sys
import os


def find_img():
    conn = lite.connect('img.sqlite3')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE captcha (img blob, capcha text)''')
    except:
	    pass
    directory =os.listdir('samples')
    for filename in directory:
        cap = filename[:5]
        fin = open('samples/'+filename, 'rb')
        img = fin.read()
        binary = lite.Binary(img)
        try:
            cursor.execute("insert into captcha values (?,?)", (binary,cap))
        except:
            pass
def prosmotr():
    conn = lite.connect('img.sqlite3')
    cursor = conn.cursor()
    sel = cursor.execute("select * from captcha")
    return sel
print(prosmotr())
# Функция открытия изображения в бинарном режиме
'''def readImage(filename):
    conn = lite.connect('udb.sqlite3')
    cursor = conn.cursor()

    try:
        fin = open('samples/'+filename, "rb")
        img = fin.read()
        return img
    finally:
        if fin:
            # Закрываем подключение с файлом
            fin.close()

try:
    # Открываем базу данных
    con = lite.connect('test.db')
    cur = con.cursor()
    # Получаем бинарные данные нашего файла
    data = readImage(find_img())
    # Конвертируем данные
    binary = lite.Binary(data)
    # Готовим запрос в базу
    cur.execute("INSERT INTO Images(Data) VALUES (?)", (binary,) )
    # Выполняем запрос
    con.commit()
finally:
    if con:
    # Закрываем подключение с базой данных
        con.close()'''