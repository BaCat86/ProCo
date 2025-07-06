import sqlite3
import db_working

# [TODO] Добавить создание готовых тегов и даже возможно связей


db_working.db_init()
connection = sqlite3.connect("old/portfolios.db")
cursor = connection.cursor()
def users():
    cursor.execute('INSERT INTO Users (login, password, email) VALUES (?, ?, ?);', ('123', '123', '123'))
    cursor.execute('INSERT INTO Users (login, password, email) VALUES (?, ?, ?);', ('bacat', '123', '123123'))
    cursor.execute('INSERT INTO Users (login, password, email) VALUES (?, ?, ?);', ('kto', 'chto', 'aga'))

def portfolios():
    cursor.execute("INSERT INTO Portfolios (userID, Name) VALUES (?, ?)", (uid, 'BaCat'))
    cursor.execute("INSERT INTO Portfolios (userID, Name) VALUES (?, ?)", (uid, 'MegaCoolDude'))
    cursor.execute("INSERT INTO Portfolios (userID, Name) VALUES (?, ?)", (uid, 'Milimitary'))
    cursor.execute("INSERT INTO Portfolios (userID, Name) VALUES (?, ?)", (uid, 'Summersay415'))
def attr():
    cursor.execute("INSERT INTO Attr (Name, desc, UID) VALUES (?, ?, ?)", ('Программирование', 'Любит прогать', uid))
    cursor.execute("INSERT INTO Attr (Name, desc, UID) VALUES (?, ?, ?)", ('Ползуновка', 'Ходит на Ползуновку',uid))
    cursor.execute("INSERT INTO Attr (Name, desc, UID) VALUES (?, ?, ?)", ('Музыка', 'Любимый трек',uid))

def tags():
    cursor.execute("INSERT INTO Tags (Name, UID) VALUES (?, ?)", ('Тег 1', uid))
    cursor.execute("INSERT INTO Tags (Name, UID) VALUES (?, ?)", ('Тег 2', uid))
    cursor.execute("INSERT INTO Tags (Name, UID) VALUES (?, ?)", ('Тег 3', uid))
# cursor.execute(f"SELECT ID FROM Users where login='123'")
# uid = cursor.fetchall()[0][0]
print('1.users\n2.portfolios\n3.attr\n4.FULL')
a = int(input("Ваш выбор: "))

def id_pol():
    cursor.execute(f"SELECT ID FROM Users where login='123'")
    uid = cursor.fetchall()[0][0]
    return uid
if a == 1:
    users()
elif a == 2:
    uid = id_pol()
    portfolios()
elif a == 3:
    uid = id_pol()
    attr()
elif a == 4:
    users()
    uid = id_pol()
    portfolios()
    attr()
    tags()

connection.commit()
