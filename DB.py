import sqlite3
from random import randint
def createdb():
    db = sqlite3.connect('users.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        FI VARCHAR(30),
        UID VARCHAR(INT)
    )""")
    db.commit()


def adddb():
    db = sqlite3.connect('qw.db')
    sql = db.cursor()
    FI = input('Введи Фамилию Имя')
    UID = randint(100000, 999999)
    sql.execute(f'INSERT INTO users (FI, UID)'
                f'VALUES (?, ?)', (FI, UID))
    db.commit()