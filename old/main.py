
import db_working as db
import act

TUD : list = [None, None] #Temporary User Data

def main(): # Точка старта
    db.db_init() # Инициализация бд (проверка, существует ли она и если нет, то создание)
    TUD[0] = entry_menu()[0]
    TUD[1] = entry_menu()[1]
    # local_id = ('0a66dd21-c2bb-4842-8d5c-e8d3af636e94', '123') # получаем что-то вроде local_id = (user_id, user_name)
    menu(TUD[0])
    
def entry_menu(): # Меню авторизации
    print(
        "[client][entry_menu]Добро пожаловать в ProCo!\nПожалуйта, выберите из списка желаемое действие:\n--------------\n0.Выход\n1.Вход\n2.Регистрация")
    try:
        a = [1, 2, 0]
        menu_an = int(input("[client][entry_menu]Ваш выбор: "))
        if menu_an in a:
            if menu_an == 1:
                _ = act.authorization()
                return _
            elif menu_an == 2:
                act.registration()
                print("[client][entry_menu]Учётная запись успешно создана") # FIX: По хорошему сделать так, что бы не недо было перезапускать скрипт
                _ = input("Нажмите ENTER, что бы продолжить...")
                _ = entry_menu()
                return _
            elif menu_an == 0:
                sys.exit()
        else:
            act.clear()
            print("Неккоректное значение ответа, попробуйте ещё раз...")
            _ = entry_menu()
            return _
    except ValueError:
        act.clear()
        print("Неккоректное значение ответа, попробуйте ещё раз...")
        _ = entry_menu()
        return _



def menu(local_id): # Меню пользователя
    act.clear()
    # [TODO] Критический баг, при возвращении в это меню программа падает, так как в функцию мы передаём только  ID пользователя, а значит и вернуть имя они - не могут
    print(
        f"[client][menu]С возвращением в ProCo, {TUD[1]}!\nВыберите из списка действие, которое хотите сделать с портфолио:\n--------------\n0. Выход\n1. Посмотреть существующее\n2. Создать новое\n3. Изменить существующее\n4. Редактировать аттрибуты\n5. Меню тегов")
    try:
        menu_an = int(input("[client][menu]Ваш выбор: "))
        act.clear()
        if menu_an == 0:
            sys.exit()
        elif menu_an == 1:
            act.portfolio_view(local_id)
        elif menu_an == 2:
            act.portfolio_create(local_id)
        elif menu_an == 3:
            portfolio_edit_menu(local_id)
        elif menu_an == 4:
            attr_menu(local_id)
        elif menu_an == 5:
            tag_menu(local_id)
        menu(local_id)
    except ValueError:
        act.clear()
        print("Неккоректное значение ответа, попробуйте ещё раз...")
        menu(local_id)

def portfolio_edit_menu(local_id):
    act.clear()
    print("Выберите действие с портфолио из списка:\n--------------\n0.Назад\n1.Посмотреть аттрибуты портфолио\n2.Редактировать значения аттрибутов\n3.Удалить аттрибут\n4.Добавить аттрибут")
    try:
        res = int(input("Ваш выбор: "))
        if res == 0:
            menu(local_id)
        elif res == 1:
            act.ptf_attr_view(local_id)
        elif res == 2:
            act.ptf_attr_val_edit(local_id)
        elif res == 3:
            act.ptf_attr_del(local_id)
        elif res == 4:
            act.ptf_attr_add(local_id)
        portfolio_edit_menu(local_id)
    except ValueError:
        portfolio_edit_menu(local_id)

def attr_menu(local_id):
    act.clear()
    print(
        "[client][attr_menu]Выберите действие с аттрибутами из списка:\n--------------\n0. Назад\n1. Создание аттрибута\n2. Удаление аттрибута\n3. Посмотреть все аттрибуты")
    try:
        menu_an = int(input("[client][attr_menu]Ваш выбор: "))
        if menu_an == 0:
            menu(local_id)
        elif menu_an == 1:
            act.attr_create(local_id)
        elif menu_an == 2:
            act.attr_del(local_id)
            _ = input('Нажмите ENTER, что бы продолжить...')
        elif menu_an == 3:
            act.attr_view(local_id)
            _ = input("Нажмите ENTER, для продолжения...")
        attr_menu(local_id)
    except ValueError:
        attr_menu(local_id)

def tag_menu(local_id):
    act.clear()
    print(
        "[client][tag_menu]Выберите действие с тегами из списка:\n--------------\n0. Назад\n1. Создание тега\n2. Удаление тега\n3. Посмотреть все теги\n4. Создать связь тега и портфолио\n5. Посмотреть портфолио с тегом")
    try:
        tag_menu_an = int(input("[client][tag_menu]Ваш выбор: "))
        if tag_menu_an == 0:
            menu(local_id)
        elif tag_menu_an == 1:
            act.tag_create(local_id)
        elif tag_menu_an == 2:
            act.tag_del(local_id)
        elif tag_menu_an == 3:
            act.tag_view(local_id)
        elif tag_menu_an == 4:
            act.ptf_tag_add(local_id)
        elif tag_menu_an == 5:
            act.ptf_tag_view(local_id)
        _ = input('Нажмите ENTER, что бы продолжить...')
        tag_menu(local_id)
    except ValueError:
        tag_menu(local_id)

if __name__ == "__main__":
    main()
