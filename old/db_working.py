import sqlite3
import sys

connection = sqlite3.connect("old/portfolios.db")
cursor = connection.cursor()
def db_init(): # Инициализация (создаёт бд, если её не существует)
    # Users
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users
    ( ID        TEXT    NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
      login     TEXT    NOT NULL UNIQUE,
      password  TEXT    NOT NULL,
      last_seen INTEGER NULL,
      email     TEXT    NOT NULL UNIQUE,
      PRIMARY KEY (ID));''')
    # print("[server][db_create]Создание таблицы Users - успешно")

    # Portfolios
    cursor.execute('''CREATE TABLE IF NOT EXISTS Portfolios
    ( -- ID портфолио
      ID       TEXT NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
      -- ID пользователя
      userID   TEXT NOT NULL,
      -- Имя портфолио
      Name     TEXT NOT NULL UNIQUE,
      -- изображение портфолио
      pictures TEXT NULL    ,
      PRIMARY KEY (ID),
      FOREIGN KEY (userID) REFERENCES Users (ID));''')
    # print("[server][db_create]Создание таблицы Portfolios - успешно")

    # Tags
    cursor.execute('''CREATE TABLE IF NOT EXISTS Tags
    ( -- ID тэга
      ID   TEXT NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
      -- Что за тэг
      Name TEXT NOT NULL,
      -- ID пользователя
      UID   TEXT NOT NULL,
      PRIMARY KEY (ID),
      FOREIGN KEY (UID) REFERENCES Users (ID)
      UNIQUE(Name, UID)
      );''')
    # print("[server][db_create]Создание таблицы Tags - успешно")

    # tagAssign
    cursor.execute('''CREATE TABLE IF NOT EXISTS tagAssign
    ( ID    TEXT NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
      -- ID (связь с) портфолио
      ptfID TEXT NOT NULL,
      -- ID (связь с) тэгом
      tagID TEXT NOT NULL,
      PRIMARY KEY (ID),
      FOREIGN KEY (tagID) REFERENCES Tags (ID),
      FOREIGN KEY (ptfID) REFERENCES Portfolios (ID));''')
    # print("[server][db_create]Создание таблицы tagAssign - успешно")

    # Attr
    cursor.execute('''CREATE TABLE IF NOT EXISTS Attr
    ( -- ID атрибута
      ID   TEXT NOT NULL DEFAULT (lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
      -- имя атрибута
      Name TEXT NOT NULL UNIQUE,
      -- Описание атрибута
      desc TEXT NULL    ,
      -- ID пользователя
      UID       TEXT NOT NULL,
      FOREIGN KEY (UID) REFERENCES Users (ID),
      PRIMARY KEY (ID));''')
    # print("[server][db_create]Создание таблицы Attr - успешно")

    # value
    cursor.execute('''CREATE TABLE IF NOT EXISTS value
    ( ID    TEXT NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
      value TEXT NULL ,
      meta  TEXT NOT NULL,
      PRIMARY KEY (ID));''')
    # print("[server][db_create]Создание таблицы value - успешно")

    # attrAssign
    cursor.execute('''CREATE TABLE IF NOT EXISTS attrAssign
    ( ID     TEXT    NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
      -- ID (cвязь с) портфолио
      ptfID  TEXT    NOT NULL,
      -- ID (связь с) атрибутом
      attrID TEXT    NOT NULL,
      -- ID значения
      vID    TEXT    NOT NULL,
      -- Положение в портфолио
      orderField  INTEGER NOT NULL,
      PRIMARY KEY (ID),
      FOREIGN KEY (ptfID) REFERENCES Portfolios (ID),
      FOREIGN KEY (attrID) REFERENCES Attr (ID),
      FOREIGN KEY (vID) REFERENCES value (ID));''')
    # print("[server][db_create]Создание таблицы attrAssign - успешно")

    # # BaseGroup
    # cursor.execute('''CREATE TABLE IF NOT EXISTS BaseGroup
    # ( -- Имя группы
    #   groupName TEXT NOT NULL,
    #   -- ID пользователя
    #   UID       TEXT NOT NULL,
    #   -- ID атрибута
    #   AID       TEXT NOT NULL,
    #   PRIMARY KEY (groupName, UID, AID),
    #   FOREIGN KEY (UID) REFERENCES Users (ID),
    #   FOREIGN KEY (AID) REFERENCES Attr (ID));''')
    # print("[server][db_create]Создание таблицы BaseGroup - успешно")

    # Создание уникальных индексов, что бы те или инные данные в таблицах не повторялись
    # cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS idx_unique_login ON Users (login);')
    # cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS idx_unique_email ON Users (email);')
    # cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS idx_unique_ptf ON Portfolios (Name);')
    # cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS idx_unique_attr ON Attr (Name);')

    connection.commit() # Изменения сохранены
    # print("[server][db_create]Изменения сохранены")
    print("[server][db_create]База данных успешно инициализирована")

def registration(data): # Сохранение в базе данных нового пользователя
    cursor.execute('INSERT INTO Users (login, password, email) VALUES (?, ?, ?);', data)
    print("[server][registration]Пользователь создан")
    connection.commit() # Изменения сохранены
    print("[server][registration]Изменения сохранены")



def authorization(data): # Авторизация пользователя (Проверка на уществование в бд, проверка доступа)
    cursor.execute("SELECT login FROM Users")
    a = cursor.fetchall() # Перебираем, что бы получить логины в человеческом виде
    b = []
    for i in range(len(a)):
        b.append(a[i][0])
    if data[0] in b:
        print("[server][authorization]Пользователь существует!")
        cursor.execute(f"SELECT password FROM Users where login='{data[0]}'")
        a = cursor.fetchall()
        if a[0][0] == data[1]:
            cursor.execute(f"SELECT ID FROM Users where login='{data[0]}'")
            res = cursor.fetchall()[0][0]
            print("[server][authorization]Авторизация успешна!")
            return res
        else:
            print("[server][authorization]Неверный пароль!")
            sys.exit()
    else:
        print("[server][authorization]Пользователя не существует!")
        sys.exit()

def portfolio_create(data): # Создание в бд нового пустого портфолио
    cursor.execute("INSERT INTO Portfolios (userID, Name) VALUES (?, ?)", data)
    connection.commit()
    print('[server][portfolio_create]Отлично, портфолио создано!')

def portfolio_choice(local_id): # Выбор портфолио (находит в бд все портфолио пользователя по его id)
    cursor.execute(f"SELECT Name, ID FROM Portfolios where userID='{local_id}'")
    res = cursor.fetchall()
    return res

def portfolio_view(ptf_id): # Получение из бд атрибутов портфолио и их значений
    cursor.execute(f"SELECT attrID FROM attrAssign where ptfID='{ptf_id}'")
    __ = cursor.fetchall()
    cursor.execute(f"SELECT vID FROM attrAssign where ptfID='{ptf_id}'")
    ___ = cursor.fetchall()
    _ = (__, ___) # Получим что-то вроде([('attrID1',), ('attrID2',), ...,('attrIDn',)], [('vID1',), ('vID2',), ..., ('vIDn',)])
    __ = []
    for i in _[0]:
        cursor.execute(f"SELECT Name, desc FROM Attr where ID='{i[0]}'")
        a = cursor.fetchall()
        __.append(a)
    ___ = []
    for i in _[1]:
        cursor.execute(f"SELECT value, meta FROM value where ID='{i[0]}'")
        a = cursor.fetchall()
        ___.append(a)
    res = (__, ___) # Получу что-то вроде ([[('attrName1', 'attrDesc1')], [('attrName2', 'attrDesc2')], ..., [('attrNameN', 'attrDescN')]], [[('value1', 'meta1')], [(value2, 'meta2')], ..., [(valueN, 'metaN')]])
    return res


def attr_create(data): # Добавление в бд аттрибута
    cursor.execute("INSERT INTO Attr (Name, desc, UID) VALUES (?, ?, ?)", data)
    connection.commit()
    print('[server][attr_create]Отлично, аттрибут создан!')

def attr_view(local_id): # Получение из бд всех аттрибутов пользователя
    cursor.execute(f"SELECT Name, desc, ID FROM Attr where UID='{local_id}'")
    a = cursor.fetchall()
    res = []
    for i in range(len(a)):
        res.append([a[i][0], a[i][1], a[i][2]])
    if res == []:
        print('[server][attr_view] У пользователя нет аттрибутов')
    return res

def ptf_attr_view(ptf_id): # Получение из бд аттрибутов этого портфолио
    cursor.execute(f"SELECT attrID FROM attrAssign where ptfID='{ptf_id}'")
    attrid = cursor.fetchall()
    a = []
    for _ in attrid:
        a.append(_[0]) # Не, ну это лютый говнокод, но иначе с этим дико не удобно работатать
    res = []
    for _ in a:
        cursor.execute(f"SELECT Name, desc, ID FROM Attr where ID='{_}'")
        res.append(cursor.fetchall())
    return res

def ptf_attr_val_edit(attr_for_edit):
    cursor.execute(f"SELECT vID FROM attrAssign where (attrID, ptfID)=('{attr_for_edit[0]}', '{attr_for_edit[1]}')")
    _ = cursor.fetchall()[0][0]
    print(_)
    cursor.execute("UPDATE value SET value = ? WHERE ID = ?", (attr_for_edit[2], _))
    connection.commit()

def attr_del(attr_id): # Полное удаление аттрибута из бд
    cursor.execute(f"DELETE FROM Attr where ID='{attr_id}'")
    connection.commit()
    print('[server][attr_del]Отлично, аттрибут удалён!')

def ptf_attr_add(ptf_id, attr_res):
    cursor.execute("INSERT INTO value (meta) VALUES (?)", ('321',))
    cursor.execute(f"SELECT ID FROM value where meta='321'") # Возможно, это стоит исправить
    _ = cursor.fetchall()
    cursor.execute(f"UPDATE value SET (meta) = (?) where ID='{_[0][0]}'", ('text',))
    data = (ptf_id, attr_res, 1, _[0][0])
    cursor.execute(f"INSERT INTO attrAssign (ptfID, attrID, orderField, vID) VALUES (?, ?, ?, ?)", data)
    connection.commit()
    print('[server][ptf_attr_add]Отлично, аттрибут привязан к портфолио!')

def ptf_attr_del(attr_id): # Удаление из бд связи между аттрибутом и портфолио
    cursor.execute(f"DELETE FROM attrAssign where attrID='{attr_id}'")
    connection.commit()
    print('[server][attr_del]Отлично, аттрибут удалён!')

def tag_view(local_id): # Получение из бд всех тегов пользователя, на вход получает что-то вроде 'userID'
    cursor.execute(f"SELECT Name, ID FROM Tags where UID='{local_id}'")
    a = cursor.fetchall()
    res = []
    for i in range(len(a)):
        res.append([a[i][0], a[i][1]])
    return res # Получим что-то вроде [['tag1', 'tag1ID'], ..., ['tagN', 'tagNID']]

def tag_create(data): # Сохранение тега в бд, принимает что-то вроде (tagName, userID)
    cursor.execute("INSERT INTO Tags (Name, UID) VALUES (?, ?)", data)
    connection.commit()
    print('[server][portfolio_create]Отлично, тег создан!')

def tag_del(tagid): # Удаление тега из бд, принимает что-то вроде tagID
    cursor.execute(f"DELETE FROM Tags where ID='{tagid}'")
    connection.commit()
    print('[server][attr_del]Отлично, тег удалён!')

def ptf_tag_add(ptf_id, tag_res):
    data = (ptf_id, tag_res)
    cursor.execute(f"INSERT INTO tagAssign (ptfID, tagID) VALUES (?, ?)", data)
    connection.commit()
    print('[server][ptf_tag_add]Отлично, аттрибут привязан к портфолио!')

def ptf_tag_view(ptf_id):
    cursor.execute(f"SELECT tagID FROM tagAssign where ptfID='{ptf_id}'")
    tagid = cursor.fetchall()
    a = []
    for _ in tagid:
        a.append(_[0]) # Не, ну это лютый говнокод, но иначе с этим дико не удобно работатать
    res = []
    for _ in a:
        cursor.execute(f"SELECT Name FROM Tags where ID='{_}'")
        res.append(cursor.fetchall())
    return res
