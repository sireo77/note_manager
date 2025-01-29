# Код по спецификации № 3.2 по Grade 1 :
# Префикс "a" обозначает локальную переменную, "t" - временную, промежуточную
# Функция обновления заметки принимает заметку (словарь) в качестве аргумента.
# Позволяет пользователю выбрать, какое поле заметки нужно обновить.
# Запрашивает новое значение для выбранного поля.
# Обновляет указанное поле заметки.
#####################################   РУКОВОДСТВО ТЕСТИРОВЩИКА   #################################################
# 1) Первый ввод - выбрать '2' - Работа с конкретной заметкой; 2) второй ввод - '3' - Поиск по порядковому номеру,
# хотя можно искать и по имени или заголовку, но номера проще запомнить; 3) третий ввод '1' - Режим редактирования заметки;
# 4) Выбор поля для уточнения; 5) Повторение по вкусу
# По коду: функция update_note - выполняет функционал обновления заметок
# функция display_note - выводит новую заметку на экран
# функция find_note - организация меню поиска заметки
# функция find_note_by_key - собственно поиск по выбранным элементам
#####################################   ОТКЛОНЕНИЕ ОТ СПЕЦИФИКАЦИИ   #################################################
# Ввод полей сделан по индексу из списка, поскольку вводить ручками очень долго. Попытка улучшить дружелюбность
# интерфейса


# Загрузка нужных модулей для работы
import ast
import datetime


#####################################   ФУНКЦИИ ОТОБРАЖЕНИЯ   #################################################

# Функция вывода меню
def show_choose_user_actions(t_menu_list):  #
    if len(t_menu_list) == 0:
        print("Список заголовков меню пуст!")
        exit()
    print("Введите цифру для выбора варианта работы:")
    for i in range(0, len(t_menu_list)):
        print(f"'{i}' - {t_menu_list[i]};")
    t_act = str(input("Выберите нужное число: > "))
    return t_act


# Функция форматированного вывода
def display_note(t_list, t_num_note):
    # t_title_list_str = nice_string_print(t_list)  # Вызов функции оформления строки вывода заголовков
    # Подробный вывод
    if t_num_note != -1:
        print(f"{t_num_note + 1}. Заголовок заметки: {t_list["1"]}")
        print(f"   Пользователь {t_list["2"]}, написал заметку: {t_list["3"]}, присвоив ей статус - '{t_list["4"]}'.")
        print(f"   Дата записи - {t_list["5"]}, cрок выполнения - {t_list["6"]}.")
    else:
        print("Внимание! Не выбрана заметка для отображения!")


# Функция форматированного отображения всех заметок
def display_notes(t_lists):  #
    print("===== Перечень заметок: =====")
    for i in range(0, len(t_lists)):
        display_note(t_lists[i], t_lists.index(t_lists[i]))



#####################################   ФУНКЦИИ ПОЛЬЗОВАТЕЛЯ   #################################################

# Функция ввода новой заметки и добавления в общий список заметок
def create_note(t_lists, t_list, t_usual_use):  # t_lists для сохранения в списке всех заметок
    print("===== Функция добавления заметок: =====")
    t_exit_allow = "1"  # Инициализация маркера выхода
    while t_exit_allow == "1":  # Сторожевое условие
        # Ввод данных о заметке
        t_list["1"] = input("Введите заголовок заметки: ")  #
        t_list["2"] = input("Введите имя пользователя: ")
        t_list["3"] = input("Введите саму заметку: ")
        t_list["4"] = status_change(t_list)  # Вызов функции изменения статуса заметки
        t_list["5"] = get_today().strftime("%d-%m-%Y") # Вызов функции сегодняшней даты
        t_need_fast_date = str(input("Задать дедлайн по текущей дате (нажмите ""1"") или выйти (любая другая)? > "))
        if t_need_fast_date == "1":
            t_list["6"] = get_today().strftime("%d-%m-%Y")
        else:
            t_list["6"] = input_date(t_list["6"], "выполнения") # Вызов функции корректного ввода дат
        if t_usual_use:  # Проверка на добовление новой или аварийное заполнение при создании файла заметок
            t_lists = append_notes(t_list) # Докидываем в список заметок новую
            t_exit_allow = str(input("Ввести ещё заметку (нажмите ""1"") или выйти (любая другая)? > "))
        else:
            # В режиме добавления новой заметки в пустой файл просто добавляем заметку в общий список и выходим
            t_lists[0] = t_list
            t_exit_allow = "0"
        print("===== Заметка добавлена =====")

    if t_usual_use:
        display_note(t_list, t_lists.index(t_list)) # Показ добавленной заметки
        save_notes(t_lists) # Загрузка в файл notes.txt
        print("===== Ввод заметок закончен =====")
    return t_list


# Функция поиска по ключу заметки из общего списка заметок
def find_note_by_key(t_lists, t_element, t_elem_type):
    for i in range(0, len(t_lists)):  # Поиск по заданному ключу
        if t_elem_type == "Имя":
            if t_element == t_lists[i]["2"]:  # Проверка на совпадение имени
                print(f'Элемент "{t_element}" присутствует в списке!')
                return t_lists[i], i  # Возвращаем заметку и её номер
        elif t_elem_type == "Заголовок":
            if t_element == t_lists[i]["1"][len(t_lists[i]["1"]) - 1]:  # Проверка совпадения с последним заголовком в списке
                print(f'Элемент "{t_element}" присутствует в списке!')
                return t_lists[i], i  # Возвращаем заметку и её номер
        elif t_elem_type == "Номер":
            if t_element == str(i + 1): # Проверка совпадения с номером заметки
                print(f'Элемент с порядковым номером №"{t_element}" присутствует в списке!')
                return t_lists[i], i # Возвращаем заметку и её номер
            else:
                if i == len(t_lists) - 1:  # Проверка на достижение конца, когда ничего не найдено
                    print("К сожалению, указанные поисковые характеристики заметки не найдены. Попробуйте ещё раз!")
                    return (), -1 # Возвращаем пустой словарь и невозможный номер

# Функция поиска заметки в общем списке заметок
def find_note(t_lists):  #
    print("===== Функция поиска заметок: =====")
    t_exit_allow = "1"  # Инициализация маркера выхода
    t_list = {}  # Изначально словарик пуст
    while t_exit_allow == "1":  # Сторожевое условие
        if len(t_lists) == 0:
            print("К сожалению, список заметок пуст. Режим поиска невозможен")
            return -1
        t_menu_list = ["Выход", "Поиск по имени пользователя", "Поиск по текущему заголовку",
                       "Поиск по порядковому номеру"]  # Настроим меню для режима поиска
        t_act = show_choose_user_actions(t_menu_list)  # Выведем меню для выбора режима работы
        if t_act == "0":  # Быстрый выход
            exit()
        elif t_act == "1":  # Поиск по имени пользователя
            t_name = input("Введите имя пользователя, заметку которого надо найти: > ")
            t_list, i = find_note_by_key(t_lists, t_name, "Имя")
            # t_exit_allow = "0"
        elif t_act == "2":  # Поиск по текущему заголовку
            t_title = input("Введите текущий заголовок, заметку с которым надо найти: > ")
            t_list, i = find_note_by_key(t_lists, t_title, "Заголовок")
            # t_exit_allow = "0"
        elif t_act == "3":  # Поиск по порядковому номеру
            t_num = input("Введите номер заметки, которую надо найти: > ")
            try:
                if int(t_num) in [0, 1000]:
                    t_num = int(t_num)
            except:
                print("Вы ввели не цифру или цифру больше 1000")
            t_list, i = find_note_by_key(t_lists, t_num, "Номер")  # Получаем заметку и её номер

        display_note(t_list, i)
        if t_list != ():    # Проверка, что какая-то заметка выбрана
            t_exit_allow = "0"
    return t_list, i  # Возвращаем найденную заметку и её номер

# Функция очистки общего списка заметок
def del_all_notes(t_lists):  #
    t_lists = []
    print("===== Список заметок очищен =====")
    save_notes(t_lists)


# Функция удаления по ключу заметки из общего списка заметок
def del_this_note(t_lists, t_element, t_elem_type):  #
    for i in range(0, len(t_lists)):  # Поиск по заданному ключу
        if t_elem_type == "Имя":
            if t_element == t_lists[i]["2"]:  # Проверка на совпадение имени
                print(f'Элемент "{t_element}" присутствует в списке!')
                del t_lists[i]  # Удаляем текущую заметку
                save_notes(t_lists)  # Грузим обрезанный список в файл
                print("===== Заметка удалена =====")
                return
        elif t_elem_type == "Заголовок":
            if t_element == t_lists[i]["1"][len(t_lists[i]["1"]) - 1]: # Проверка совпадения с последним заголовком в списке
                print(f'Элемент "{t_element}" присутствует в списке!')
                del t_lists[i]  # Удаляем текущую заметку
                save_notes(t_lists)  # Грузим обрезанный список в файл
                print("===== Заметка удалена =====")
                return
    print("К сожалению, указанные поисковые характеристики заметки не найдены. Попробуйте ещё раз!")


# Функция удаления заметки в общем списке заметок
def del_note(t_lists):  #
    print("===== Функция удаления заметок по ключам: =====")
    t_exit_allow = "1"  # Инициализация маркера выхода
    while t_exit_allow == "1":  # Сторожевое условие
        if len(t_lists) == 0:
            print("К сожалению, список заметок пуст. Режим удаления невозможен")
            return
        t_menu_list = ["Выход", "Поиск для удаления по имени", "Поиск для удаления по текущему заголовку",
                       "Удаление всех заметок"]   # Настроим меню для режима удаления
        t_act = show_choose_user_actions(t_menu_list)  # Выведем меню для выбора режима работы
        if t_act == "0":  # Быстрый выход
            exit()
        elif t_act == "1":  # Удаление по имени
            t_name = input("Введите имя пользователя, заметку которого надо удалить: > ")
            del_this_note(t_lists, t_name, "Имя")
        elif t_act == "2":  # Удаление по текущему заголовку
            t_title = input("Введите текущий заголовок, заметку с которым надо удалить: > ")
            del_this_note(t_lists, t_title, "Заголовок")
        elif t_act == "3":  # Удаление всех
            del_all_notes(t_lists)
            print("Режим удаления более невозможен. ")
            return
        else:
            print("Вы ввели некорректное число, режим не был активирован.")

        t_exit_allow = str(input("Удалить ещё заметку (нажмите ""1"") или выйти (любая другая) > "))

    print("===== Удаление заметок завершено =====")
    save_notes(t_lists)


def update_note(t_list, t_key):
    print("===== Редактирование заметки: =====")
    t_names = ("Заголовок", "Имя пользователя" , "Содержание заметки" , "Статус заметки" ,
               "Время создания" , "Срок выполнения" )  # Настроим кортеж отображаемых элементов
    t_exit_allow = "1"  # Инициализация маркера выхода
    while t_exit_allow == "1":  # Сторожевое условие
        # Просмотр и изменение данных о заметке
        print("Выберите цифру с номером поля заметки, значение которого требуется изменить:")
        for i in range(0, len(t_names)):  # Прокручиваем в цикле словарь с полями заметки
            t_sep = ""
            t_punct_mark = lambda t_sep: "." if i == len(t_names) - 1 else ";"  # Определим знак препинания

            print(f"{t_names[i]}: {t_list[str(i + 1)]} - цифра '{i+1}'{t_punct_mark(t_sep)}")
        # t_menu_list
        # show_choose_user_actions(t_menu_list)
        t_act = '0'
        while t_act not in ['1', '2', '3', '4', '5', '6']:
            t_act = str(input("Выберите нужное число: > "))
            if t_act not in  ['1', '2', '3', '4', '5', '6']:
                print(f"Должна быть цифра в диапазоне от 0 до {len(t_names)}. Повторите ввод!")
        if t_act == "4": # Если работаем со статусом
            t_list[t_act] = status_change(t_list)
        elif t_act in ["5", "6"]: # Если работаем со временем
            t_list[t_act] = input_date(t_list[t_act], "")
        else:
            t_list[t_act] = input(f"Введите {t_names[int(t_act) - 1]}: > ")  # Если вводим имя и содержание

        t_lists = exchange_notes(t_list, t_key)  # Заменяем в списке заметок нужную по индексу
        print("===== Заметка добавлена =====")
        display_note(t_list, t_key)  # Выводим результат на экран
        t_exit_allow = str(input("Продолжить работу с заметкой (нажмите ""1"") или выйти (любая другая)? > "))
    print("===== редактирование заметок завершено =====")
    save_notes(t_lists)

# Функция изменения статуса заметки
def status_change(t_list):
    t_status_list = ("в процессе", "выполнено", "отложено")  # Кортеж возможных статусов заметки
    t_exit_allow = False  # Инициализация маркера выхода из режима выбора статуса
    while not t_exit_allow:
        print(f"Для уточнения статуса нажмите: 1 - статус '{t_status_list[0]}', "
              f"2 - статус '{t_status_list[1]}', 3 - статус '{t_status_list[2]}'.")
        t_stst_num = str(input("Выберите число ""1"", ""2"" или ""3"": > "))
        if t_stst_num == "1":
            t_list["4"] = t_status_list[0]
            t_exit_allow = True
        elif t_stst_num == "2":
            t_list["4"] = t_status_list[1]
            t_exit_allow = True
        elif t_stst_num == "3":
            t_list["4"] = t_status_list[2]
            t_exit_allow = True
        else:
            print("Вы ввели некорректное значение. Повторите ввод, пожалуйста!")
    return t_list["4"]  # Возвращаем значение статуса - одно из кортежа


#####################################  СЕРВИСНЫЕ ФУНКЦИИ  #################################################

# Функция для получения текущей даты
def get_today():
    t_date = datetime.datetime.now()
    return t_date


# Функция для расчёта разницы между датами
def quant_days(t_list):
    t_day_count = abs((datetime.datetime.strptime(t_list["6"], "%d-%m-%Y") - get_today()).days)
    return t_day_count


# Функция для обработки пользовательского ввода дат
def input_date(t_date, t_definition):
    t_exit_allow = False  # Инициализация маркера выхода
    while not t_exit_allow:
        t_date = input(
            f'Введите дату {t_definition} в формате (dd-mm-yyyy), используя ""-"" в качестве разделителя: > ')
        # date_object = datetime.datetime.strptime("01-01-2025", "%d-%m-%Y").date()
        # Проверка того, что ввод был в нужном формате без вылета из программы
        try:
            t_exit_allow = True  # Разрешаем выход, если нет ошибки
            date_object = datetime.datetime.strptime(t_date, "%d-%m-%Y").date()  # Проверка, что выдержан формат даты
        except:
            t_exit_allow = False  # Запрещаем выход из цикла, пока есть ошибка
            print("Вы ввели ошибочную дату, поэтому повторите попытку!")
    succes_date_string = date_object.strftime("%d-%m-%Y")
    print(f"Введена дата {succes_date_string}. Она соответствует формату.")
    return succes_date_string


# Функция проверки срока выполнения в текущей записи
def data_check(t_list):
    print(f"Дедлайн по текущей заметке - {t_list["5"]}.")
    # Сравним дату с текущей
    if datetime.datetime.strptime(t_list["6"], "%d-%m-%Y") < get_today():  # Если меньше
        print(f"Срок истёк. Просрочка составляет дней: {(quant_days(t_list))}.")
    elif datetime.datetime.strptime(t_list["6"], "%d-%m-%Y") == get_today():  # Если равна
        print(f"Сегодня дедлайн! Нужно поторопиться!.")
    else:
        print(f"Срок ещё не наступил. До дедлайна осталось дней: {(quant_days(t_list))}.") # Если дедлайн не наступил
    return t_list


# Функция проверка наличия заметок note в списке заметок notes
def check_notes_in_list():  #
    t_list_not_empty = False
    t_lists = load_notes()
    if len(t_lists) > 0:
        t_list_not_empty = True
    else:
        print("Файл с заметками не найден")
    return t_list_not_empty


# Функция замены заметки note в списке заметок notes
def exchange_notes(t_list, t_key):  # Первый аргумент общий список notes, второй - note
    t_lists = load_notes()
    t_lists[t_key] = t_list
    return t_lists


# Функция добавления заметки note в список заметок notes
def append_notes(t_list):  # Первый аргумент общий список notes, второй - note
    t_lists = load_notes()
    t_lists.append(t_list)
    return t_lists


#####################################  ФУНКЦИИ ПО РАБОТЕ С ФАЙЛОМ  #################################################

# Функция сохранения переменной notes в промежуточном файле notes.txt
def save_notes(t_lists):
    with open('notes.txt', 'w+') as f:
        f.write(str(t_lists))


# Функция выгрузки списка из промежуточного файла notes.txt
def load_notes():
    t_list = {"1": [], "2": "", "3": "", "4": "", "5": "", "6": ""}
    t_lists = [t_list]  # Значение списка заметок по умолчанию
    try:
        t_file = open('notes.txt', 'r+')
    except IOError:
        print("Файл с заметками не обнаружен! Создаём новый.")
        with open('notes.txt', 'w+') as t_file:
            t_list = create_note(t_lists, t_list, False)
            t_str = str(t_lists)
            t_file.write(t_str)
    else:
        t_str = t_file.read()
    t_lists = ast.literal_eval(t_str)  # преобразуем строку в список
    return t_lists


# -= ТЕКСТ ПРОГРАММЫ =-
# Объявление списков

a_note = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": ""}  # Словарь для хранения одной заметки
a_notes = []  # Список всех заметок
a_ses_exit_allow = "1"  # Инициализация маркера выхода из программы


print("Приветствую Вас! Данная программа позволит работать с заметками.")
# Основной цикл программы, демонстрирующий меню для работы
while a_ses_exit_allow == "1":
    if check_notes_in_list():  # Проверяем наличие заметок note в списке заметок notes
        a_notes = load_notes()  # Загружаем заметки из файла, чтобы не возиться со вводом
        display_notes(a_notes)  # Демонстрируем чего у нас в справочнике

    a_menu_list = ["Выход", "Работа со списком заметок", "Работа с конкретной заметкой"] # Настроим главное меню
    a_main_act = show_choose_user_actions(a_menu_list)  # Выводим меню для выбора режима работы
    if a_main_act == "0":  # Быстрый выход
        exit()
    elif a_main_act == "1":  # Работа со списком заметок
        print("===== Работа со списком заметок =====")
        a_menu_list = ["Выход", "Режим добавления новой заметки", "Режим отображения всех заметок",
                       "Режим удаления заметки"]    # Настроим меню работы со списком заметок
        a_act = show_choose_user_actions(a_menu_list)  # Выведем меню для выбора режима работы
        if a_act == "0":  # Быстрый выход
            exit()
        elif a_act == "1":  # Режим ввода новой заметки
            a_note = create_note(a_notes, a_note, True)
        elif a_act == "2":  # Режим отображения всех заметок
            display_notes(a_notes)
        elif a_act == "3":  # Режим удаления заметки
            del_note(a_notes)
        else:
            print("Вы ввели некорректное число, режим не был активирован.")
    elif a_main_act == "2":  # Работа с конкретной заметкой
        print("===== Работа с конкретной заметкой =====")
        a_note, a_ind_of_note = find_note(a_notes)  # Входим в режим поиска заметки, чтобы было с чем работать
        a_menu_list = ["Выход", "Режим редактирования заметки","Режим работы со статусом заметки",
                       "Режим работы с датами заметки"]   # Настроим меню работы о заметкой
        a_act = show_choose_user_actions(a_menu_list)  # Выведем меню для выбора режима работы
        if a_act == "0": # Быстрый выход
             exit()
        elif a_act == "1": # Режим редактирования заметки
            update_note(a_note, a_ind_of_note)   # Запускаем режим редактирования
        elif a_act == "2": # Режим работы со статусом заметки
            print(f"Статус текущей заметки - {a_note["4"]}.")
            a_note["4"] = status_change(a_note)
        elif a_act == "3":# Режим работы с датами заметки
            a_note = data_check(a_note)
        else:
            print("Вы ввели некорректное число, режим не был активирован.")
    else:
        print("Вы ввели некорректное число, режим не был активирован.")

    a_ses_exit_allow = str(input("Продолжить работу в программе (нажмите ""1"") или выйти (любая другая)? > "))

