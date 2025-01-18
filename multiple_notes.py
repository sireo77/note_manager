# Код по спецификации № 2.4 по Grade 1:
# Префикс "a" обозначает локальную переменную, "t" - временную, промежуточную

# Загрузка нужных модулей для работы
import ast, datetime

# Функция заполнения списка заголовков
def TitlesInput(t_list):
    t_exit_allow = "1"  # Инициализация маркера выхода из режима ввода заголовков
    # Цикл ввода заголовков
    t_title_count = 0 # Инициализация числа заголовков
    t_title_list = t_list[5]
    while t_exit_allow == "1": # Сторожевое условие
        t_title = input("Введите заголовок заметки №" + str(t_title_count + 1) + ": ")
        t_title_list.append(t_title)
        t_title_count = t_title_count + 1
        t_exit_allow = str(input("Продолжить (нажмите ""1"") или выйти (нажмите ""2"")"))
        if t_exit_allow not in ["1", "2"]: # Проверка введённой цифры.
            t_exit_allow = "1"
            print("Вы ввели некорректное число, поэтому ввод заголовков будет продолжен")
    t_list[5] = t_title_list # Внесение списка заголовков в список заметок note
    t_list[6] = t_title_count # Внесение числа заголовков
    return t_list

# Функция оформления строки вывода заголовков
def NiceSringPrint(t_list):
    t_title_list_str = ""  # Пустая строка для создания красивого вывода
    t_title_count = t_list[6] # Инициализация числа заголовков
    # Цикл для заполнения строки заголовков с пояснениями
    for i in range(0, t_title_count):
        if i == 0:
            t_title_list_str = t_title_list_str + "Заголовок №1 - " + t_list[5][0] + "; "
        else:
            t_title_list_str = t_title_list_str + "заголовок №" + str(i + 1) + " - " + t_list[5][i] + "; "
    t_title_list_str = t_title_list_str[:-2] + "."  # Меняем точку с запятой на точку в конце предложения
    return t_title_list_str

# Функция изменения статуса заметки
def StatusChange(t_list):
    t_exit_allow = False # Инициализация маркера выхода из режима выбора статуса
    while not t_exit_allow:
        print(f"Для уточнения статуса нажмите: 1 - статус '{a_status_list[0]}', "
              f"2 - статус '{a_status_list[1]}', 3 - статус '{a_status_list[2]}'.")
        t_stst_num = str(input("Выберите число ""1"", ""2"" или ""3"":  "))
        if t_stst_num == "1":
            t_list[2] = a_status_list[0]
            t_exit_allow = True
        elif t_stst_num == "2":
            t_list[2] = a_status_list[1]
            t_exit_allow = True
        elif t_stst_num == "3":
            t_list[2] = a_status_list[2]
            t_exit_allow = True
        else:
            print("Вы ввели некорректное значение. Повторите ввод, пожалуйста!")
    return t_list[2]

# Функция сохранения переменной notes в промежуточном файле notes.txt
def SaveNotes(t_list):
    with open('notes.txt', 'w+') as f:
        f.write(str(t_list))

# Функция выгрузки списка из промежуточного файла notes.txt
def LoadNotes():
    with open('notes.txt', 'r+') as f:
        t_str = f.read()
    t_list = ast.literal_eval(t_str) # преобразуем строку в список
    return t_list

# Функция добавления заметки note в список заметок notes
def AppendNotes(t_lists, t_list): # Первый аргумент общий список notes, второй - note
    t_lists.append(t_list)
    return t_lists

# Функция вывода меню
def ShowAndChooseUserActions(t_act): #
    t_exit_allow = False  # Инициализация маркера выхода из режима выбора статуса
    while not t_exit_allow:
        print("Варианты работы с заметками следующие, нажав кнопку: ")
        print("'1' - ввести новую заметку; ")
        print("'2' - работа со статусом заметки; ")
        print("'3' - работа с датами заметки.")
        t_act = str(input("Выберите число ""1"", ""2"" или ""3"":  "))
        if t_act in ["1","2","3"]:
            t_exit_allow = True
        else:
            print("Вы ввели некорректное значение. Повторите ввод, пожалуйста!")
            t_exit_allow = False
    return t_act

# Функция форматированного вывода
def ShowNote(t_list):
    t_title_list_str = ""  # Пустая строка для создания красивого вывода
    t_title_count = t_list[6] # Инициализация числа заголовков
    t_title_list_str = NiceSringPrint(t_list) # Вызов функции оформления строки вывода заголовков
    # Подробный вывод
    print("Содержимое заметки:")
    print(f"Пользователь {t_list[0]}, написал заметку о {t_list[1]}, присвоив ей статус - '{t_list[2]}'.")
    print(f"Дата записи (кратк.) - {t_list[3][:5]}, cрок выполнения (кратк.) - {t_list[4][:5]}.")
    print(f"Cписок заголовков заметки: {t_title_list_str}")

# Функция ввода новой заметки
def NewNote(t_lists, t_list): #t_lists пока не используется
    # Ввод данных о заметке
    t_list_in = t_list
    t_list_in[0] = input("Введите имя пользователя: ")
    t_list_in[1] = input("Введите саму заметку: ")
    t_list_in[2] = StatusChange(t_list_in) # Вызов функции изменения статуса заметки
    t_list_in[3] = input("Введите дату создания, используя '/' в качестве разделителя: ")
    t_list_in[4] = input("Введите срок выполнения, используя '/' в качестве разделителя: ")
    t_list_in = TitlesInput(t_list_in) # Вызов функции заполнения списка заголовков
    print(t_list_in)
    ShowNote(t_list_in)

    # Здесь будет добавление note в notes, заливка в файл, очистка текущей note
    # Временно код попроще, только для 1 заметки
    SaveNotes(t_list_in)

    t_list = t_list_in
    # return t_title_count

# Функция для получения текущей даты
def GetToday(t_date):
    t_date = datetime.date.today()
    return t_date

# Функция для расчёта разницы между датами


# Функция для обработки пользовательского ввода


# Функция ввода новой заметки
def DataChange(t_lists, t_list):
    t_exit_allow = "1"  # Инициализация маркера выхода из программы
    t_list = LoadNotes()

    # Основной цикл программы, демонстрирующий меню для работы
    while t_exit_allow == "1":
        ShowNote(t_list)


        t_exit_allow = str(input("Продолжить работу с датами (нажмите ""1"") или выйти (нажмите ""2"")"))
        if t_exit_allow not in ["1", "2"]:  # Проверка введённой цифры.
            t_exit_allow = "1"
            print("Вы ввели некорректное число, поэтому работа с датами будет продолжена")
    return t_list

# Объявление списков
a_title_list = []                                         # Вложенный список для заголовков
a_status_list = ("в процессе","выполнено","отложено")     # Кортеж возможных статусов заметки
a_note = ["", "", "в процессе", "", "", a_title_list, 0]  # Список для хранения одной заметки, 7-й элемент - число заголовков
a_notes = []                                              # Список всех заметок
a_ses_exit_allow = "1"  # Инициализация маркера выхода из программы
# a_title_count = 0  # Инициализация счётчика заголовков

# Примечание тестировщику: поскольку режим сохранения в файл пока не реализован, то
# следует сначала выбрать в меню "1", т.е. ввод новой заметки, а затем
# выбрать "3", т.е. работать с её датами.
# Пока мер по очистке пока нет и в переменной a_note будет введённая заметка

# Основной цикл программы, демонстрирующий меню для работы
while a_ses_exit_allow == "1" :
    a_act = "1" # По умолчанию предполагается ввод новой заявки
    a_act = ShowAndChooseUserActions(a_act) # Выведем меню для выбора режима работы
    if a_act == "1": # Режим ввода новой заметки
        NewNote(a_notes, a_note)
    elif a_act == "2": # Режим работы со статусом заметки
        print("Извините, данный режим пока не доступен") # Здесь пока заглушка
    elif a_act == "3":# Режим работы с датами заметки
        a_note = DataChange(a_notes, a_note)



    a_ses_exit_allow = str(input("Продолжить работу с заметками (нажмите ""1"") или выйти (нажмите ""2"")"))
    if a_ses_exit_allow not in ["1", "2"]:  # Проверка введённой цифры.
        a_ses_exit_allow = "1"
        print("Вы ввели некорректное число, поэтому работа с заметкой будет продолжена")