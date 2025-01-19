# Код по спецификации № 2.3 по Grade 1:
# Префикс "a" обозначает локальную переменную, "t" - временную, промежуточную

# Загрузка нужных модулей для работы
import  datetime


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
    print(f"Дата записи (кратк.) - {t_list[3][:5]}, cрок выполнения (кратк.) - {t_list[4][:5]}.")



# Функция для получения текущей даты
def GetToday():
    t_date = datetime.datetime.now()
    return t_date

# Функция для расчёта разницы между датами
def QuantDays(t_list):
    t_day_count = abs((datetime.datetime.strptime(t_list[4], "%d-%m-%Y") - GetToday()).days)
    return t_day_count

# Функция для обработки пользовательского ввода
def InputData(t_date):
    t_exit_allow = False  # Инициализация маркера выхода
    while not t_exit_allow:
        t_date = input('Введите дату в формате (dd-mm-yyyy), используя ""-"" в качестве разделителя: ')
        date_object = datetime.datetime.strptime("01-01-2025", "%d-%m-%Y").date()
        try:
            t_exit_allow = True
            date_object = datetime.datetime.strptime(t_date, "%d-%m-%Y").date()
        except:
            t_exit_allow = False
            print("Вы ввели ошибочную дату, поэтому повторите попытку!")
    succes_date_string = date_object.strftime("%d-%m-%Y")
    print(f"Введена дата {succes_date_string}. Она соответствует формату.")
    return succes_date_string

# Функция проверки срока выполнения
def DataCheck(t_lists, t_list):
    t_exit_allow = "1"  # Инициализация маркера выхода из режима проверки
    #
    while t_exit_allow == "1":
        if datetime.datetime.strptime(t_list[4], "%d-%m-%Y") < GetToday():  #
            print(f"Срок истёк. Просрочка составляет дней: {(QuantDays(t_list))}.")
        elif datetime.datetime.strptime(t_list[4], "%d-%m-%Y") == GetToday():  #
            print(f"Сегодня дедлайн! Нужно поторопиться!.")
        else:
            print(f"Срок ещё не наступил. До дедлайна осталось дней: {(QuantDays(t_list))}.")
            t_exit_allow = False

        t_exit_allow = str(input("Продолжить работу с датами (нажмите ""1"") или выйти (нажмите ""2"") >> "))
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

# Примечание тестировщику: поскольку режим сохранения в файл пока не реализован, то
# следует сначала выбрать в меню "1", т.е. ввод новой заметки, а затем
# выбрать "3", т.е. работать с её датами.
# Пока мер по очистке пока нет и в переменной a_note будет введённая заметка

# Основной цикл программы, демонстрирующий меню для работы
while a_ses_exit_allow == "1" :
    a_act = "1" # По умолчанию предполагается ввод новой заявки
    #  Пока ввод будет ограниченным: только даты
    a_act = ShowAndChooseUserActions(a_act)
    if a_act == "1":  # Режим ввода новой заметки
        a_note[3] = InputData(a_note[3])
        a_note[4] = InputData(a_note[4])
        ShowNote(a_note)
    elif a_act == "2": # Режим работы со статусом заметки
        print("Извините, данный режим в данном задании отключен") # Здесь пока заглушка
    elif a_act == "3":# Режим работы с датами заметки
        a_note = DataCheck(a_notes, a_note)
        # ShowNote(a_note)

    a_ses_exit_allow = str(input("Продолжить работу с заметками (нажмите ""1"") или выйти (нажмите ""2"") >> "))
    if a_ses_exit_allow not in ["1", "2"]:  # Проверка введённой цифры.
        a_ses_exit_allow = "1"
        print("Вы ввели некорректное число, поэтому работа с заметкой будет продолжена")