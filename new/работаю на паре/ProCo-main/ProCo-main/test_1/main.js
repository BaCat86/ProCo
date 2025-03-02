const sqlite3 = require('sqlite3').verbose(); //подключаем библиотеку для работы с sqlite3
const inquirer = require('inquirer');//подключаем библиотеку для работы с inquirer
const db = new sqlite3.Database('./test.db');//Открываем файл с БД (эта переменная, по сути является ссылкой на db)

function dbcreate() {
    db.serialize(() => {
        db.run(`CREATE TABLE IF NOT EXISTS Users
(
  ID        TEXT    NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
  login     TEXT    NOT NULL,
  password  TEXT    NOT NULL,
  last_seen INTEGER NULL,
  email     TEXT    NOT NULL,
  PRIMARY KEY (ID)
);`) //Создаём таблицу Users
        db.run(`CREATE TABLE IF NOT EXISTS Portfolios
(
  -- ID портфолио
  ID       TEXT NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
  -- ID пользователя
  userID   TEXT NOT NULL,
  -- Имя портфолио
  Name     TEXT NOT NULL,
  -- изображение портфолио
  pictures TEXT NULL    ,
  PRIMARY KEY (ID),
  FOREIGN KEY (userID) REFERENCES Users (ID)
);`) //Создаём таблицу Portfolios
        db.run(`CREATE TABLE IF NOT EXISTS Tags
(
  -- ID тэга
  ID   TEXT NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
  -- Что за тэг
  Name TEXT NOT NULL,
  PRIMARY KEY (ID)
);`)
    db.run(`CREATE TABLE IF NOT EXISTS tagAssign
(
  ID    TEXT NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
  -- ID (связь с) портфолио
  ptfID TEXT NOT NULL,
  -- ID (связь с) тэгом
  tagID TEXT NOT NULL,
  PRIMARY KEY (ID),
  FOREIGN KEY (tagID) REFERENCES Tags (ID),
  FOREIGN KEY (ptfID) REFERENCES Portfolios (ID)
);`) //Создаём таблицу tagAssign
    db.run(`CREATE TABLE IF NOT EXISTS Attr
(
  -- ID атрибута
  ID   TEXT NOT NULL DEFAULT (lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
  -- имя атрибута
  Name TEXT NOT NULL,
  -- Описание атрибута
  desc TEXT NULL    ,
  PRIMARY KEY (ID)
);`) //Создаём таблицу Attr
    db.run(`CREATE TABLE IF NOT EXISTS value
(
  ID    TEXT NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
  value TEXT NULL    ,
  meta  TEXT NOT NULL,
  PRIMARY KEY (ID)
);`) //Создаём таблицу value
    db.run(`CREATE TABLE IF NOT EXISTS attrAssign
(
  ID     TEXT    NOT NULL DEFAULT(lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)))),
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
  FOREIGN KEY (vID) REFERENCES value (ID)
);
`) //Создаём таблицу attrAssign
    db.run(`CREATE TABLE IF NOT EXISTS BaseGroup
(
  -- Имя группы
  groupName TEXT NOT NULL,
  -- ID пользователя
  UID       TEXT NOT NULL,
  -- ID атрибута
  AID       TEXT NOT NULL,
  PRIMARY KEY (groupName, UID, AID),
  FOREIGN KEY (UID) REFERENCES Users (ID),
  FOREIGN KEY (AID) REFERENCES Attr (ID)
);
`) //Создаём таблицу BaseGroup
    }
  )
}

dbcreate()
