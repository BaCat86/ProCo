CREATE TABLE Users (
  User_ID  INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  login     TEXT    NOT NULL,
  password  TEXT    NOT NULL,
  last_seen TEXT	NULL,
  email     TEXT    NOT NULL
);

-- пользователи и информация о них

CREATE TABLE Portfolios (
  ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  userID INT NOT NULL,
  Name TEXT NOT NULL,
  pictures TEXT,
  FOREIGN KEY (userID) REFERENCES Users (User_ID)
);

-- К кажодому пользователю призязано свое портфолио (на отдельного человека)
-- В портфолио есть данные о Названии, Изображении, и ссылки на другие атрибуты и теги

CREATE TABLE Tags (
  ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  Name TEXT NOT NULL
);

-- Тег - основа группирования портфолио

CREATE TABLE tagAssign
(
  ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  ptfID INT NOT NULL,
  tagID INT NOT NULL,
  FOREIGN KEY (tagID) REFERENCES Tags (ID),
  FOREIGN KEY (ptfID) REFERENCES Portfolios (ID)
);

-- связка тега и портфолио

create table AttributeKeys (
 ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
 NAME TEXT NOT NULL,
 DESCRIPTION TEXT
);

-- AttributeKeys - предназначена для обращения к атрибута (титульник атрибута)

CREATE TABLE AttributeAssign (
  ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  ptfID  INT    NOT NULL,
  attrID INT    NOT NULL,
  NumberOfAttribute  INT NOT NULL,
  ValueAttr TEXT, 
  FOREIGN KEY (ptfID) REFERENCES Portfolios (ID),
  FOREIGN KEY (attrID) REFERENCES AttributeKeys (ID)
);

-- AttributeAssign - для связи портфолио и его атрибутов, а также для нумерации атрибутов в каждом отдельном портфолио, хранит значения аттрибутов

 -- 1. Человек N
--  - атрибут 1 - цвет кожи - белый
--  - атрибут 2 - цвет глаз - коричневый
--  - атрибут 3 - работа - аналитик данных