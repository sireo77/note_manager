# Код по спецификации № 2.5 по Grade 1:
# Префикс "a" обозначает локальную переменную, "t" - временную, промежуточную

# Загрузка нужных модулей для работы
import ast
import datetime


# Функция оформления строки вывода заголовков
# По заданию нужно отображать только последний заголовок, поэтому функция не требуется
# def nice_string_print(t_list):
#     t_title_list_str = ""  # Пустая строка для создания красивого вывода
#     t_title_count = len(t_list["6"])  # Получение числа заголовков
#     # Цикл для заполнения строки заголовков с пояснениями
#     for i in range(0, t_title_count):
#         if i == 0:
#             t_title_list_str = t_title_list_str + "Заголовок №1 - " + t_list["6"][0] + "; "
#         else:
#             t_title_list_str = t_title_list_str + "заголовок №" + str(i + 1) + " - " + t_list["6"][i] + "; "
#     t_title_list_str = t_title_list_str[:-2] + "."  # Меняем точку с запятой на точку в конце предложения
#     return t_title_list_str


# Функция вывода меню
def show_choose_user_actions(t_menu_list):  #
    if len(t_menu_list) == 0:
        print("Список заголовков меню пуст!")
        exit()
    print("Введите цифру для выбора варианта работы с заметками:")
    for i in range(0, len(t_menu_list)):
        print(f"'{i}' - {t_menu_list[i]};")
    t_act = str(input("Выберите нужное число: > "))
    return t_act


# Функция форматированного вывода
def show_note(t_list, t_num_note):
    # t_title_list_str = nice_string_print(t_list)  # Вызов функции оформления строки вывода заголовков
    # Подробный вывод
    print(f"{t_num_note + 1}. Текущий заголовок заметки: {t_list["6"][len(t_list["6"])-1]}")
    print(f"   Пользователь {t_list["1"]}, написал заметку о {t_list["2"]}, присвоив ей статус - '{t_list["3"]}'.")
    print(f"   Дата записи - {t_list["4"]}, cрок выполнения - {t_list["5"]}.")


# Функция форматированного отображения всех заметок
def show_all_notes(t_lists):  #
    print("===== Перечень заметок: =====")
    for i in range(0, len(t_lists)):
        show_note(t_lists[i], t_lists.index(t_lists[i]))
        # return t_act


# Функция заполнения списка заголовков
# Идея в том, чтобы хранить историю заголовков и возвращать последний
def titles_input(t_list):
    t_exit_allow = "1"  # Инициализация маркера выхода из режима ввода заголовков
    # Цикл ввода заголовков
    t_title_count = 0  # Инициализация числа заголовков
    t_title_list = t_list["6"]
    print("Введите историю заголоовков - от старых к новым:")
    while t_exit_allow == "1":  # Сторожевое условие
        t_title = input("Введите заголовок заметки №" + str(t_title_count + 1) + ": ")
        t_title_list.append(t_title)
        t_title_count = t_title_count + 1
        t_exit_allow = str(input("Продолжить ввод заголовков (нажмите ""1"") или выйти (нажмите ""2"") > "))
        if t_exit_allow not in ["1", "2"]:  # Проверка введённой цифры.
            t_exit_allow = "1"
            print("Вы ввели некорректное число, поэтому ввод заголовков будет продолжен")
    t_list["6"] = t_title_list  # Внесение списка заголовков в список заметок note
    return t_list


# Функция ввода новой заметки и добавления в общий список заметок
def new_note(t_lists, t_list):  # t_lists пока не используется
    print("===== Функция добавления заметок: =====")
    t_exit_allow = "1"  # Инициализация маркера выхода
    while t_exit_allow == "1":  # Сторожевое условие
        # Ввод данных о заметке
        t_list_in = t_list
        t_list_in["1"] = input("Введите имя пользователя: ")
        t_list_in["2"] = input("Введите саму заметку: ")
        t_list_in = titles_input(t_list_in)  # Вызов функции заполнения списка заголовков
        t_list_in["3"] = status_change(t_list_in)  # Вызов функции изменения статуса заметки
        t_list_in["4"] = input_date(a_note["4"], "создания заметки")
        t_list_in["5"] = input_date(a_note["5"], "выполнения")
        t_lists = append_notes(t_lists, t_list_in)
        show_note(t_list_in, t_lists.index(t_list_in))
        t_exit_allow = str(input("Ввести ещё заметку (нажмите ""1"") или выйти (любая другая) > "))
    print("===== Ввод заметок закончен =====")
    save_notes(t_lists)


# Функция удаления заметки в общем списке заметок
def del_note(t_lists, t_list):  #
    print("===== Функция удаления заметок по ключам: =====")
    print("Извините, данная функция пока не доступна")
    # t_exit_allow = "1"  # Инициализация маркера выхода
    # while t_exit_allow == "1":  # Сторожевое условие
    #
    # print("===== Удаление заметок завершено =====")
    # save_notes(t_lists)

# Функция изменения статуса заметки
def status_change(t_list):
    t_exit_allow = False  # Инициализация маркера выхода из режима выбора статуса
    while not t_exit_allow:
        print(f"Для уточнения статуса нажмите: 1 - статус '{a_status_list[0]}', "
              f"2 - статус '{a_status_list[1]}', 3 - статус '{a_status_list[2]}'.")
        t_stst_num = str(input("Выберите число ""1"", ""2"" или ""3"": > "))
        if t_stst_num == "1":
            t_list["3"] = a_status_list[0]
            t_exit_allow = True
        elif t_stst_num == "2":
            t_list["3"] = a_status_list[1]
            t_exit_allow = True
        elif t_stst_num == "3":
            t_list["3"] = a_status_list[2]
            t_exit_allow = True
        else:
            print("Вы ввели некорректное значение. Повторите ввод, пожалуйста!")
    return t_list["3"]


# Функция для получения текущей даты
def get_today():
    t_date = datetime.datetime.now()
    return t_date


# Функция для расчёта разницы между датами
def quant_days(t_list):
    t_day_count = abs((datetime.datetime.strptime(t_list["5"], "%d-%m-%Y") - get_today()).days)
    return t_day_count


# Функция для обработки пользовательского ввода дат
def input_date(t_date, t_definition):
    t_exit_allow = False  # Инициализация маркера выхода
    while not t_exit_allow:
        t_date = input(
            f'Введите дату {t_definition} в формате (dd-mm-yyyy), используя ""-"" в качестве разделителя: > ')
        date_object = datetime.datetime.strptime("01-01-2025", "%d-%m-%Y").date()
        # Проверка того, что ввод был в нужном формате без вылета из программы
        try:
            t_exit_allow = True  # Разрешаем выход, если нет ошибки
            date_object = datetime.datetime.strptime(t_date, "%d-%m-%Y").date()
        except:
            t_exit_allow = False  # Запрещаем выход из цикла, пока есть ошибка
            print("Вы ввели ошибочную дату, поэтому повторите попытку!")
    succes_date_string = date_object.strftime("%d-%m-%Y")
    print(f"Введена дата {succes_date_string}. Она соответствует формату.")
    return succes_date_string


# Функция проверки срока выполнения в текущей записи
def data_check(t_list):
    if datetime.datetime.strptime(t_list["5"], "%d-%m-%Y") < get_today():  #
        print(f"Срок истёк. Просрочка составляет дней: {(quant_days(t_list))}.")
    elif datetime.datetime.strptime(t_list["5"], "%d-%m-%Y") == get_today():  #
        print(f"Сегодня дедлайн! Нужно поторопиться!.")
    else:
        print(f"Срок ещё не наступил. До дедлайна осталось дней: {(quant_days(t_list))}.")
    return t_list


# Функция сохранения переменной notes в промежуточном файле notes.txt
def save_notes(t_lists):
    with open('notes.txt', 'w+') as f:
        f.write(str(t_lists))


# Функция выгрузки списка из промежуточного файла notes.txt
def load_notes():
    with open('notes.txt', 'r+') as f:
        t_str = f.read()
    t_lists = ast.literal_eval(t_str)  # преобразуем строку в список
    return t_lists


# Функция добавления заметки note в список заметок notes
def append_notes(t_lists, t_list):  # Первый аргумент общий список notes, второй - note
    t_lists = load_notes()
    t_lists.append(t_list)
    return t_lists


# Функция проверка наличия заметок note в списке заметок notes
def check_notes_in_list():  #
    t_list_not_empty = False
    t_lists = load_notes()
    if len(t_lists) > 0:
        t_list_not_empty = True
    return t_list_not_empty


def edit_note(t_list):
    print("===== Редактирование заметки: =====")


# -= ТЕКСТ ПРОГРАММЫ =-
# Объявление списков
a_title_list = []  # Вложенный список для заголовков
a_status_list = ("в процессе", "выполнено", "отложено")  # Кортеж возможных статусов заметки
a_note = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": a_title_list}  # Словарь для хранения одной заметки
a_notes = []  # Список всех заметок
a_ses_exit_allow = "1"  # Инициализация маркера выхода из программы

# Основной цикл программы, демонстрирующий меню для работы
print("Приветствую Вас! Данная программа позволит работать с заметками.")
if check_notes_in_list():
    a_notes = load_notes()  # Загружаем заметки из файла, чтобы не возиться со вводом
    show_all_notes(a_notes)  # Демонстрируем чего у нас в справочнике
while a_ses_exit_allow == "1":
    a_act = "1"  # По умолчанию предполагается ввод новой заявки
    a_menu_list = ["Выход", "Работа со списком заметок", "Работа с конкретной заметкой"]
    a_main_act = show_choose_user_actions(a_menu_list)  # Выведем меню для выбора режима работы
    if a_main_act == "0":  # Быстрый выход
        exit()
    elif a_main_act == "1":  # Работа со списком заметок
        print("===== Работа со списком заметок =====")
        a_menu_list = ["Выход", "Режим добавления новой заметки", "Режим отображения всех заметок",
                       "Режим удаления заметки"]
        a_act = show_choose_user_actions(a_menu_list)  # Выведем меню для выбора режима работы
        if a_act == "0":  # Быстрый выход
            exit()
        elif a_act == "1":  # Режим ввода новой заметки
            new_note(a_notes, a_note)
        elif a_act == "2":  # Режим отображения всех заметок
            show_all_notes(a_notes)
        elif a_act == "3":  # Режим удаления заметки
            print("Извините, данный режим пока не доступен")  # Здесь пока заглушка
        else:
            print("Вы ввели некорректное число, режим не был активирован.")
            t_exit_allow = False
    elif a_main_act == "2":  # Работа с конкретной заметкой
        print("===== Работа с конкретной заметкой =====")
        print("Извините, данный режим пока не доступен")
        # a_menu_list = ["Выход", "Режим редактирования заметки","Режим работы со статусом заметки","Режим работы с датами заметки"]
        # a_act = show_choose_user_actions(a_menu_list)  # Выведем меню для выбора режима работы
        # Здесь будет поиск заметки по ??? и работа с нею
        # if a_act == "0": # Быстрый выход
        #     exit()
        # elif a_act == "1": # Режим редактирования заметки
        #     edit_note(a_note)
        # elif a_act == "2": # Режим работы со статусом заметки
        #     print("Извините, данный режим пока не доступен") # Здесь пока заглушка
        #     # a_note = status_change(a_note)
        # elif a_act == "3":# Режим работы с датами заметки
        #     print("Извините, данный режим пока не доступен")  # Здесь пока заглушка
        #     # a_note = data_change(a_note)
        # else:
        #     print("Вы ввели некорректное число, режим не был активирован.")
        #     t_exit_allow = False
    else:
        print("Вы ввели некорректное число, режим не был активирован.")
        t_exit_allow = False

    a_ses_exit_allow = str(input("Продолжить работу с заметками (нажмите ""1"") или выйти (нажмите ""2"") > "))
    if a_ses_exit_allow not in ["1", "2"]:  # Проверка введённой цифры.
        a_ses_exit_allow = "1"
        print("Вы ввели некорректное число, поэтому работа с заметкой будет продолжена.")
