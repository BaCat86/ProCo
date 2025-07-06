### ПОЛЛЬЗОВАТЕЛЬ ДОБАВЛЯЕТ ДАННЫЕ В ПОРТФОЛИО ИЛИ ТЕГАХ

INSERT INTO [TABLE] ([ARGS]) VALUES (?, ?, ?);

### ПОЛЬЗОВАТЕЛЬ ИЗМЕНЯЕТ ДАННЫЕ В ПОРТФОЛИО ИЛИ ТЕГАХ

UPDATE [TABLE] SET [ARGS] = ? WHERE [ID_CONDITION]

### ПОЛЬЗОВАТЕЛЬ УДАЛЯЕТ ДАННЫЕ В ПОРТФОЛИО ИЛИ ТЕГАХ

DELETE FROM [TABLE] WHERE [ID_CONDITION]

### ПОЛЬЗОВАТЕЛЬ ФИЛЬТРУЕТ ПО ТЕГАМ
SELECT distinct Portfolios.Name from  
Portfolios join tagAssign on Portfolios.ID = tagAssign.ptfID
join Tags on Tags.ID = tagAssign.tagID
where Tags in [ARGS] - только по конкретным тегам 

### ПОЛЬЗОВАТЕЛЬ ФИЛЬТРУЕТ ПО АТРИБУТАМ

SELECT distinct Portfolios.Name from  
Portfolios join AttributeAssign on Portfolios.ID = AttributeAssign.ptfID
join AttributeKeys on AttributeAssign.attrID =  AttributeKeys.ID
where AttributeAssign.ValueAttr in [ARGS] 
-- только по конкретным Атрибутам например по месту работы

###  ПОЛЬЗОВАТЕЛЬ ФИЛЬТРУЕТ ПО АТРИБУТАМ И ПО ТЕГАМ

SELECT Tags.Name_tag, Portfolios.Name from  
Portfolios join AttributeAssign on Portfolios.ID = AttributeAssign.ptfID
join AttributeKeys on AttributeAssign.attrID =  AttributeKeys.ID
join tagAssign on Portfolios.ID = tagAssign.ptfID
join Tags on Tags.ID = tagAssign.tagID

where Tags in [ARGS] and AttributeAssign.ValueAttr  in [ARGS]
