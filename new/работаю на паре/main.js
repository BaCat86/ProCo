const sqlite3 = require('sqlite3').verbose(); //подключаем библиотеку для работы с sqlite3
// const inquirer = require('inquirer');//подключаем библиотеку для работы с inquirer
const db = new sqlite3.Database('./test.db');//Открываем файл с БД (эта переменная, по сути является ссылкой на db)

function dbcreate() {
  db.serialize(() => {
    db.run(`CREATE TABLE IF NOT EXISTS Users
(
  -- ID пользователя(значение по умолчанию - uuid v4)
  ID        TEXT    NOT NULL DEFAULT lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))),
  -- логин пользователя
  login     TEXT    NOT NULL,
  -- Пароль для доступа
  password  TEXT    NOT NULL,
  -- Время последнего посещения
  last_seen INTEGER NULL     DEFAULT Проще латы хранить в виде чисел: https://metanit.com/sql/sqlite/6.3.php,
  -- Почта нужна для восстановления пароля
  email     TEXT    NOT NULL,
  PRIMARY KEY (ID)
);`) //Создаём таблицу Users
    db.run(`CREATE TABLE IF NOT EXISTS Portfolios
(
  -- ID портфолио
  ID       TEXT NOT NULL DEFAULT lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))),,
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
  ID   TEXT NOT NULL DEFAULT lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))),,
  -- Что за тэг
  Name TEXT NOT NULL,
  PRIMARY KEY (ID)
);`)
  })
  db.run(`CREATE TABLE IF NOT EXISTS tagAssign
(
  ID    TEXT NOT NULL DEFAULT lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))),,
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
  ID   TEXT NOT NULL DEFAULT lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))),,
  -- имя атрибута
  Name TEXT NOT NULL,
  -- Описание атрибута
  desc TEXT NULL    ,
  PRIMARY KEY (ID)
);`) //Создаём таблицу Attr
  db.run(`CREATE TABLE IF NOT EXISTS value
(
  -- ID значения
  ID    TEXT NOT NULL DEFAULT lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))),,
  -- само значение
  value TEXT NULL    ,
  -- что это за значение
  meta  TEXT NOT NULL,
  PRIMARY KEY (ID)
);`) //Создаём таблицу value
  db.run(`REATE TABLE IF NOT EXISTS attrAssign
(C
  ID     TEXT    NOT NULL DEFAULT lower(hex(randomblob(4)) || '-' || hex(randomblob(2)) || '-' || '4' || substr(hex(randomblob(2)), 2) || '-' || substr('89AB', 1 + (abs(random()) % 4), 1) || substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))),,
  -- ID (cвязь с) портфолио
  ptfID  TEXT    NOT NULL,
  -- ID (связь с) атрибутом
  attrID TEXT    NOT NULL,
  -- ID значения
  vID    TEXT    NOT NULL,
  -- Положение в портфолио
  order  INTEGER NOT NULL,
  PRIMARY KEY (ID),
  FOREIGN KEY (ptfID) REFERENCES Portfolios (ID),
  FOREIGN KEY (attrID) REFERENCES Attr (ID),
  FOREIGN KEY (vID) REFERENCES value (ID)
);`) //Создаём таблицу attrAssign
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

dbcreate()

function getAllTables() {
  return new Promise(function (resolve, reject) {
    db.all("select name from sqlite_master where type='table'", (err, rows) => {
      if (err) {
        reject(err);
      }
      resolve(rows);
    });
  });
}

function getUser(login, password) {
  userid = db.get(`SELECT * FROM Users WHERE login = ? AND password = ?`, [login, password], (err, row) => {
    if (err) {
      throw err
    }
    console.log(err)
  })
  return "1"
}

function getPortfolios(tables, userid) {
  return db.get(`SELECT * FROM Portfolios WHERE userId = ?`, [userid], (err, row) => {
    if (err) {
      throw err
    }
    console.log(err)
  })
}

async function main() {
  let tables = (await getAllTables()).map((e) => e['name']).filter((e) => e != "sqlite_sequence")

}


try {
  main();
} catch (ex) {
  console.log(ex);
}

