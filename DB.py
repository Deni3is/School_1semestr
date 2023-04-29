#by Gleb//
import sqlite3
from random import randint
def createdb():
    db = sqlite3.connect('users.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        FI VARCHAR(50),
        UID INT
    )""")
    db.commit()


def adddb():
    db = sqlite3.connect('users.db')
    sql = db.cursor()
    FI = input('Введи Фамилию Имя: ')
    UID = randint(100000, 999999)
    sql.execute(f'INSERT INTO users (FI, UID)'
                f'SELECT * FROM users (FI, UID)'
                f'VALUES (?, ?)', (FI, UID))
    db.commit()



def checkUIDinDB():
    db = sqlite3.connect('users.db')
    sql = db.cursor()
    UIDcheck = int(input('Введи UID: '))
    sql.execute(f"SELECT UID FROM users WHERE UID = '{UIDcheck}'")
    if sql.fetchone() is None:
        return UIDcheck
    else:
        return 0
    db.commit()



while(1):
    key = int(input('1 - Создание БД\n'
                    '2 - Добавление в БД\n'
                    '3 - Проверка UID в БД\n'))

    if key == 1:
        createdb()
    elif key == 2:
        adddb()
    elif key == 3:
        print(checkUIDinDB())
    else:
        break