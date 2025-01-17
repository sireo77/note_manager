# Полный код по спецификации № 2.2 по Grade 1:
# Префикс "a" обозначает локальную переменную, "t" - временную, промежуточную

# Функция заполнения списка заголовков
def TitlesInput(t_note, t_title_count):
    t_exit_allow = "1"  # Инициализация маркера выхода из режима ввода заголовков
    t_score = t_title_count
    # Цикл ввода заголовков
    while t_exit_allow == "1": # Сторожевое условие
        t_title_list = t_note[5]
        t_title = input("Введите заголовок заметки №" + str(t_score + 1) + ": ")
        t_title_list.append(t_title)
        t_score = t_score + 1
        t_exit_allow = str(input("Продолжить (нажмите ""1"") или выйти (нажмите ""2"")"))
        if t_exit_allow not in ["1", "2"]: # Проверка введённой цифры.
            t_exit_allow = "1"
            print("Вы ввели некорректное число, поэтому ввод заголовков будет продолжен")
    t_note[5] = t_title_list # Внесение данных в список заметок a_note)
    return t_score

# Функция оформления строки вывода заголовков
def NiceSringPrint(t_note, t_title_count):
    t_title_list_str = ""  # Пустая строка для создания красивого вывода
    # Цикл для заполнения строки заголовков с пояснениями
    for i in range(0, t_title_count):
        if i == 0:
            t_title_list_str = t_title_list_str + "Заголовок №1 - " + t_note[5][0] + "; "
        else:
            t_title_list_str = t_title_list_str + "заголовок №" + str(i + 1) + " - " + t_note[5][i] + "; "
    t_title_list_str = t_title_list_str[:-2] + "."  # Меняем точку с запятой на точку в конце предложения
    return t_title_list_str

# Функция изменения статуса заметки
def StatusChange(t_note):
    t_exit_allow = False # Инициализация маркера выхода из режима выбора статуса
    while not t_exit_allow:
        print(f"Для уточнения статуса нажмите: 1 - статус '{a_status_list[0]}', "
              f"2 - статус '{a_status_list[1]}', 3 - статус '{a_status_list[2]}'.")
        t_stst_num = str(input("Выберите число ""1"", ""2"" или ""3"": "))
        if t_stst_num == "1":
            t_note[2] = a_status_list[0]
            t_exit_allow = True
        elif t_stst_num == "2":
            t_note[2] = a_status_list[1]
            t_exit_allow = True
        elif t_stst_num == "3":
            t_note[2] = a_status_list[2]
            t_exit_allow = True
        else:
            print("Вы ввели некорректное значение. Повторите ввод, пожалуйста!")
    return t_note[2]

# Объявление списков
a_title_list = []                                      # Вложенный список для заголовков
a_status_list = ("в процессе","выполнено","отложено")  # Кортеж возможных статусов заметки
a_note = ["", "", "в процессе", "", "", a_title_list]  # Основной список для хранения заметки

a_ses_exit_allow = "1"  # Инициализация маркера выхода из программы
a_first_iteration = True

while a_ses_exit_allow == "1" :
    # Ввод данных о заметке
    if a_first_iteration:
        a_note[0] = input("Введите имя пользователя: ")
        a_note[1] = input("Введите саму заметку: ")
    else:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print("Работа со статусом заметки:")

    print(f"Текущий статус заметки - '{a_note[2]}'.")
    a_note[2] = StatusChange(a_note) # Вызов функции изменения статуса заметки

    #  // Закрыто, поскольку не требуется по заданию
    #a_note[3] = input("Введите дату создания, используя '/' в качестве разделителя: ")
    #a_note[4] = input("Введите срок выполнения, используя '/' в качестве разделителя: ")

    # Закрыто, поскольку не требуется по заданию
    # a_title_count = 0  # Инициализация счётчика заголовков
    # a_title_count = TitlesInput(a_note, a_title_count) # Вызов функции заполнения списка заголовков
    # a_title_list_str = ""  # Пустая строка для создания красивого вывода
    # a_title_list_str = NiceSringPrint(a_note, a_title_count) # Вызов функции оформления строки вывода заголовков

    # Подробный вывод
    print("Содержимое заметки:")
    print(f"Пользователь {a_note[0]}, написал заметку о {a_note[1]}, присвоив ей статус - '{a_note[2]}'.")

    # // Закрыто, поскольку не требуется по заданию
    # print(f"Дата записи (кратк.) - {a_note[3][0:5]}, cрок выполнения (кратк.) - {a_note[4][0:5]}.")
    # print(f"Cписок заголовков заметки: {a_title_list_str}")

    a_first_iteration = False
    a_ses_exit_allow = str(input("Продолжить (нажмите ""1"") или выйти (нажмите ""2"")"))
    if a_ses_exit_allow not in ["1", "2"]:  # Проверка введённой цифры.
        a_ses_exit_allow = "1"
        print("Вы ввели некорректное число, поэтому работа с заметкой будет продолжена")