__author__ = 'roman'

import sqlite3 as lite
d = {}
def dobavlenie_usera():
    print('name: ')
    name = str(input())
    score = input()
    d[name] = score
    print(d)

def dobavlenie_score(d):
    name = input()
    score = int(input())
    a = int(d.get(name))
    a = a + score
    d[name] = a
    return d
def redact_file():
    d2 = {}
    with open('b.txt') as inp:
        for i in inp.readlines():
            key,val = i.strip().split(':')
            d2[key] = val
    print(d2)
    dobavlenie_score(d2)
    print(d2)
    with open('b.txt','w') as out:
        for key,val in d2.items():
            out.write('{}:{}\n'.format(key,val))

def create():
    conn = lite.connect('users.sqlite3')
    cursor = conn.cursor()
    sel = cursor.execute('''CREATE TABLE users (user text, score int, balance int, invite int)''')
    return
def stat():
    conn = lite.connect('users.sqlite3')
    cursor = conn.cursor()
    sel = cursor.execute('''select * from users''')
    row = sel.fetchall()
    print(row)
def drop():
    conn = lite.connect('users.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''drop table users''')
create()