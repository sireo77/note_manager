# Код по спецификации № 3.4 по Grade 1 :
# Префикс "a" обозначает локальную переменную, "t" - временную, промежуточную
# Функция поиска принимает список заметок, элемент (заголовок, имя, ключевое слово или статус) и тип поиска.
# Возвращает список заметок, соответствующих критериям поиска.
# Выводит результаты в структурированном формате.
#####################################   РУКОВОДСТВО ТЕСТИРОВЩИКА   #################################################
# 1) Первый ввод - '1' - Работа со списком заметок; 2) второй ввод - '3' - Режим вывода отобранных заметок;
# 3) Третий ввод - '3' - Поиск по ключевому слову или '4' - Поиск по статусу; 4) Вывод на экран заметок
# Есть аналогичная функция, которая позволяет поиск по ряду ключей, но только 1 заметки. Для неё путь:
# 1) Первый ввод - '2' - "Работа с конкретной заметкой"; 2) далее автоматически открывается режим настройки
# поиска конкретной строки
# По коду:
# функция search_a_lot_of_notes - выполняет поиск заметки по заголовку, имени, ключевому слову или статусу
# функция search_by_any_criterio - позволяет по нескольким ключам выбрать список заметок, допускается ввод части
# текста поля, например, для имени "Иванов Иван" только "Иван". Но "Иван" в заголовке и др. полях функция не найдёт.
# find_notes - управляет организацией поиска
# функции search_notes и find_note делают аналогичное, но возвращают 1 заметку и её индекс в списке


# Загрузка нужных модулей для работы
import ast
import datetime
from colorama import init, Fore


####################################   ФУНКЦИИ ОТОБРАЖЕНИЯ   #################################################
##############################################################################################################

# Функция вывода меню (настраиваемая)
def show_choose_user_actions(t_menu_list):  #
    if len(t_menu_list) == 0:
        print("Список заголовков меню пуст!")
        exit()
    print("Введите цифру для выбора элемента меню':")
    for i in range(0, len(t_menu_list)):
        print(f"'{i}' - {t_menu_list[i]};")
    t_act = str(input("Выберите нужное число: > "))
    return t_act


# Функция форматированного вывода
def display_note(t_list, t_num_note):
    # Подробный вывод
    init()
    if t_num_note != -1:
        print(Fore.GREEN + f"Заметка №{t_num_note + 1}:")
        print(Fore.YELLOW + f"Заголовок заметки: {t_list["1"]}\n"
              f"Имя пользователя {t_list["2"]};\n"
              f"Описание: {t_list["3"]};\n"
              f"Статус - '{t_list["4"]}';\n"
              f"Дата создания - {t_list["5"]};\n"
              f"Дедлайн - {t_list["6"]}.")
    else:
        print("Внимание! Не выбрана заметка для отображения!")
    print(Fore.RESET + "=============================")


# Функция форматированного отображения всех заметок
def display_notes(t_lists):  #
    print("===== Перечень заметок: =====")
    if len(t_lists) > 5:
        print("Список слишком большой. Будут отображены последние 5 заметок.")
        for i in range(len(t_lists) - 5, len(t_lists)):
            display_note(t_lists[i], t_lists.index(t_lists[i]))
    else:
        for i in range(0, len(t_lists)):
            display_note(t_lists[i], t_lists.index(t_lists[i]))


#####################################   ФУНКЦИИ ПОЛЬЗОВАТЕЛЯ   #################################################

# Функция ввода новой заметки и добавления в общий список заметок
def create_note(t_lists, t_list, t_usual_use):  # t_lists для сохранения в списке всех заметок
    print("===== Функция добавления заметок: =====")
    t_exit_allow = "1"  # Инициализация маркера выхода
    while t_exit_allow == "1":  # Сторожевое условие
        # Ввод данных о заметке
        print(len(t_lists))
        t_list["1"] = title_unique_input(t_lists)
        t_list["2"] = input("Введите имя пользователя: ")
        t_list["3"] = input("Введите саму заметку: ")
        t_list["4"] = status_change()  # Вызов функции изменения статуса заметки
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
        print("===== Заметка добавлена =====")  #

    if t_usual_use:
        display_note(t_list, t_lists.index(t_list)) # Показ добавленной заметки
        save_notes(t_lists) # Загрузка в файл notes.txt
        print("===== Ввод заметок закончен =====")
    return t_list


# Функция поиска по нескольким ключам заметки из общего списка заметок. Используется логика "ИЛИ", т.е. по любому
# совпавшему критерию
def search_by_any_criterio(t_lists, t_element):
    t_find_lists = []  # Переменная для множественного поиска

    for i in range(0, len(t_lists)):  # Поиск по заданным ключам
        for j in range(0, len(t_element["Text"])):
            t_substr = t_element["Text"][j]
            t_str = str(t_lists[i].values())
            if t_str.find(t_substr) != -1:  # Проверка совпадения с частью или целым элементом в списке
                if t_lists[i] not in t_find_lists:  # Проверка, что такой заметки ещё нет в найденном
                    print(f'Элемент "{t_element["Text"][j]}" присутствует в списке!')
                    t_find_lists.append(t_lists[i])
                    print()

    # Проверка на достижение конца, когда ничего не найдено
    if len(t_find_lists) > 0:
        # print(t_find_lists)
        return t_find_lists
    else:
        print("К сожалению, указанные поисковые характеристики заметки не найдены. Попробуйте ещё раз!")
        return () # Возвращаем пустой словарь и невозможный номер

# Функция поиска по ключу заметки из общего списка заметок
def search_a_lot_of_notes(t_lists, t_element, t_elem_type):
    t_find_lists = []  # Переменная для множественного поиска
    for i in range(0, len(t_lists)):  # Поиск по заданному ключу
        if t_elem_type == "Имя":
            if t_element == t_lists[i]["2"]:  # Проверка на совпадение имени
                print(f'Заметка от пользователя "{t_element}" присутствует в списке!')
                t_find_lists.append(t_lists[i])
        elif t_elem_type == "Заголовок":
            if t_element == t_lists[i]["1"]:  # Проверка совпадения с  заголовком в списке
                print(f'Заметка с заголовком "{t_element}" присутствует в списке!')
                t_find_lists.append(t_lists[i])
        elif t_elem_type == "Слово":
            if str(t_lists[i]).find(str(t_element)) != -1:  # Проверка совпадения с частью или целым элементом в списке
                print(f'Элемент "{t_element}" присутствует в списке!')
                t_find_lists.append(t_lists[i])
        elif t_elem_type == "Статус":
            if t_element == t_lists[i]["4"]:  # Проверка совпадения со статусом
                print(f'Заметка со статусом "{t_element}" присутствует в списке!')
                t_find_lists.append(t_lists[i])
    # Проверка на достижение конца, когда ничего не найдено
    if len(t_find_lists) > 0:
        # print(t_find_lists)
        return t_find_lists
    else:
        print("К сожалению, указанные поисковые характеристики заметки не найдены. Попробуйте ещё раз!")
        return () # Возвращаем пустой словарь и невозможный номер


# Функция поиска подмножества заметок в общем списке заметок
def find_notes(t_lists):  #
    print("===== Функция поиска заметок: =====")
    t_exit_allow = "1"  # Инициализация маркера выхода
    t_find_crit = {"Key": [], "Text": []}  # Переменная для списка критериев поиска для множественного поиска
    t_find_lists = []  # Переменная для результатов поиска
    while t_exit_allow == "1":  # Сторожевое условие
        if len(t_lists) == 0:
            print("К сожалению, список заметок пуст. Режим поиска невозможен")
            return []
        t_menu_list = ["Выход", "Поиск по имени пользователя",
                       "Поиск по текущему заголовку", "Поиск по ключевому слову",
                       "Поиск по статусу", "Поиск по нескольким ключам"]  # Настроим меню для режима поиска
        t_menu_list_by_any_criterio = ("Заголовок", "Имя пользователя", "Содержание заметки", "Статус заметки",
                       "Время создания", "Срок выполнения")  # Настроим кортеж отображаемых элементов
        t_act = show_choose_user_actions(t_menu_list)  # Выведем меню для выбора режима работы
        if t_act == "0":  # Быстрый выход
            exit()
        elif t_act == "1":  # Поиск по имени пользователя
            t_name = input("Введите имя пользователя, заметку которого надо найти: > ")
            t_find_lists = search_a_lot_of_notes(t_lists, t_name, "Имя")
        elif t_act == "2":  # Поиск по текущему заголовку
            t_title = input("Введите текущий заголовок, заметку с которым надо найти: > ")
            t_find_lists = search_a_lot_of_notes(t_lists, t_title, "Заголовок")
        elif t_act == "3":  # Поиск по ключевому словуу
            t_title = input("Введите ключевое слово, заметку с которым надо найти: > ")
            t_find_lists = search_a_lot_of_notes(t_lists, t_title, "Слово")
        elif t_act == "4":  # Поиск по статусу
            t_title = status_change()
            t_find_lists = search_a_lot_of_notes(t_lists, t_title, "Статус")
        elif t_act == "5":  # Поиск по нескольким ключам
            print(f"При вводе можно вводить часть поля, например, первые слова.\n"
                  "Введите нужные ключевые слова:")
            for i in range(0, len(t_lists[0])):
                t_ask = input(f"По полю '{t_menu_list_by_any_criterio[i]}' искать (нажмите ""1"") или нет (любая другая)?: > ")
                if t_ask == "1":
                    t_input_string = input(f"Введите текст в поле '{t_menu_list_by_any_criterio[i]}': > ")
                    t_find_crit["Key"].append(i)
                    t_find_crit["Text"].append(t_input_string)

            if len(t_find_crit["Text"]) == 0:
                print("Не заданы критерии поиска!")
            else:
                t_find_lists = search_by_any_criterio(t_lists, t_find_crit)
        display_notes(t_find_lists)
        if t_find_lists != ():    # Проверка, что какая-то заметка выбрана
            t_exit_allow = "0"
    return t_find_lists  # Возвращаем найденную заметку и её номер


# Функция поиска по ключу заметки из общего списка заметок
def search_notes(t_lists, t_element, t_elem_type):
    for i in range(0, len(t_lists)):  # Поиск по заданному ключу
        if t_elem_type == "Номер":
            if t_element == str(i + 1): # Проверка совпадения с номером заметки
                print(f'Заметка с порядковым номером №"{t_element}" присутствует в списке!')
                return t_lists[i], i # Возвращаем заметку и её номер
        elif t_elem_type == "Имя":
            if t_element == t_lists[i]["2"]:  # Проверка на совпадение имени
                print(f'Заметка от пользователя "{t_element}" присутствует в списке!')
                return t_lists[i], i  # Возвращаем заметку и её номер
        elif t_elem_type == "Заголовок":
            if t_element == t_lists[i]["1"]:  # Проверка совпадения с  заголовком в списке
                print(f'Заметка с заголовком "{t_element}" присутствует в списке!')
                return t_lists[i], i  # Возвращаем заметку и её номер
        elif t_elem_type == "Слово":
            if str(t_lists[i]).find(str(t_element)) != -1:  # Проверка совпадения с частью или целым элементом в списке
                print(f'Элемент "{t_element}" присутствует в списке!')
                return t_lists[i], i  # Возвращаем заметку и её номер
        elif t_elem_type == "Статус":
            if t_element == t_lists[i]["4"]:  # Проверка совпадения со статусом
                print(f'Заметка со статусом "{t_element}" присутствует в списке!')
                return t_lists[i], i  # Возвращаем заметку и её номер
    # Проверка на достижение конца, когда ничего не найдено
    print("К сожалению, указанные поисковые характеристики заметки не найдены. Попробуйте ещё раз!")
    return (), -1 # Возвращаем пустой словарь и невозможный номер


# Функция поиска 1 заметки в общем списке заметок. Ищет первое вхождение
def find_note(t_lists):  #
    print("===== Функция поиска заметок: =====")
    t_exit_allow = "1"  # Инициализация маркера выхода
    t_list = {}  # Изначально словарик пуст
    while t_exit_allow == "1":  # Сторожевое условие
        if len(t_lists) == 0:
            print("К сожалению, список заметок пуст. Режим поиска невозможен")
            return -1
        t_menu_list = ["Выход", "Поиск по порядковому номеру", "Поиск по имени пользователя",
                       "Поиск по текущему заголовку", "Поиск по ключевому слову",
                       "Поиск по статусу"]  # Настроим меню для режима поиска
        t_act = show_choose_user_actions(t_menu_list)  # Выведем меню для выбора режима работы
        if t_act == "0":  # Быстрый выход
            exit()
        elif t_act == "1":  # Поиск по порядковому номеру
            t_num = input("Введите номер заметки, которую надо найти: > ")
            try:
                if int(t_num) in [0, 1000]:
                    t_num = int(t_num)
            except:
                print("Вы ввели не цифру или цифру больше 1000")
            t_list, i = search_notes(t_lists, t_num, "Номер")  # Получаем заметку и её номер
        elif t_act == "2":  # Поиск по имени пользователя
            t_name = input("Введите имя пользователя, заметку которого надо найти: > ")
            t_list, i = search_notes(t_lists, t_name, "Имя")
        elif t_act == "3":  # Поиск по текущему заголовку
            t_title = input("Введите текущий заголовок, заметку с которым надо найти: > ")
            t_list, i = search_notes(t_lists, t_title, "Заголовок")
        elif t_act == "4":  # Поиск по текущему заголовку
            t_title = input("Введите ключевое слово, заметку с которым надо найти: > ")
            t_list, i = search_notes(t_lists, t_title, "Слово")
        elif t_act == "5":  # Поиск по текущему заголовку
            t_title = status_change()
            t_list, i = search_notes(t_lists, t_title, "Статус")
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
def del_notes(t_lists):  #
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
    t_menu_list = ("Возврат в главное меню", "Заголовок", "Имя пользователя" , "Содержание заметки" , "Статус заметки" ,
               "Время создания" , "Срок выполнения" )  # Настроим кортеж отображаемых элементов
    t_exit_allow = "1"  # Инициализация маркера выхода
    while t_exit_allow == "1":  # Сторожевое условие
        # Просмотр и изменение данных о заметке
        print("Выберите номер поля заметки, которое будет уточнено")
        t_act = show_choose_user_actions(t_menu_list)  # Выведем меню для выбора режима работы
        if t_act == '0':
            return
        while t_act not in ['1', '2', '3', '4', '5', '6']:
            t_act = str(input("Выберите нужное число: > "))
            if t_act not in  ['1', '2', '3', '4', '5', '6']:
                print(f"Должна быть цифра в диапазоне от 0 до {len(t_menu_list)}. Повторите ввод!")
        if t_act == "4": # Если работаем со статусом
            t_list[t_act] = status_change()
        elif t_act in ["5", "6"]: # Если работаем со временем
            t_list[t_act] = input_date(t_list[t_act], "")
        else:
            t_list[t_act] = input(f"Введите {t_menu_list[int(t_act)]}: > ")  # Если вводим имя и содержание
        t_lists = exchange_notes(t_list, t_key)  # Заменяем в списке заметок нужную по индексу
        print("===== Заметка добавлена =====")
        display_note(t_list, t_key)  # Выводим результат на экран
        t_exit_allow = str(input("Продолжить работу с заметкой (нажмите ""1"") или выйти (любая другая)? > "))
    print("===== Hедактирование заметок завершено =====")
    save_notes(t_lists)

# Функция изменения статуса заметки
def status_change():
    t_status_list = ("в процессе", "выполнено", "отложено", "новая")  # Кортеж возможных статусов заметки
    t_exit_allow = False  # Инициализация маркера выхода из режима выбора статуса
    t_status = "в процессе"
    while not t_exit_allow:
        print(f"Для уточнения статуса нажмите: 1 - статус '{t_status_list[0]}', "
              f"2 - статус '{t_status_list[1]}', 3 - статус '{t_status_list[2]}', "
              f"4 - статус '{t_status_list[3]}'.")
        t_stst_num = str(input("Выберите число ""1"", ""2"", ""3"" или ""4"": > "))
        if t_stst_num in ["1", "2", "3", "4"]:
            t_status = t_status_list[int(t_stst_num) - 1]
            print(f"Новый статус: {t_status}.")
            t_exit_allow = True
        else:
            print("Вы ввели некорректное значение. Повторите ввод, пожалуйста!")
    return t_status  # Возвращаем значение статуса - одно из кортежа


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
def check_notes_in_list() -> bool:  #
    t_lists = load_notes()
    if len(t_lists) > 0:
        return True
    else:
        print("Файл с заметками не найден или пуст")
        return False


# Функция ввода уникального заголовка
def title_unique_input(t_lists) -> str:  # Указание на то, что вернётся содержимое поля "Заголовок"
    t_not_exist_allow = True
    while t_not_exist_allow:
        t_not_exist_allow = False
        t_title_name = input("Введите заголовок заметки: ")  #
        for i in range(len(t_lists)):
            if t_lists[i]["1"] == t_title_name:
                print("Такой заголовок уже есть. Введите другой!")
                t_not_exist_allow = True
                break
    return t_title_name


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
a_set_of_notes = [] # Подмножество заметок, отобранных по критерию

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
                       "Режим вывода отобранных заметок","Режим удаления заметки"]    # Настроим меню работы со списком заметок
        a_act = show_choose_user_actions(a_menu_list)  # Выведем меню для выбора режима работы
        if a_act == "0":  # Быстрый выход
            exit()
        elif a_act == "1":  # Режим ввода новой заметки
            a_note = create_note(a_notes, a_note, True)  # Вызов в обычном режиме с сохранением
        elif a_act == "2":  # Режим отображения всех заметок
            display_notes(a_notes)
        elif a_act == "3":  # Режим отображения заметок, отобранных по критерию
            a_set_of_notes = find_notes(a_notes)
        elif a_act == "4":  # Режим удаления заметки
            del_notes(a_notes)
        else:
            print("Вы ввели некорректное число, режим не был активирован.")
    elif a_main_act == "2":  # Работа с конкретной заметкой
        print("===== Работа с конкретной заметкой =====")
        a_note, a_ind_of_note = find_note(a_notes)  # Входим в режим поиска заметки, чтобы было с чем работать
        a_menu_list = ["Выход", "Режим редактирования заметки","Режим работы со статусом заметки",
                       "Режим проверки дедлайна заметки", "Режим поиска заметки"]   # Настроим меню работы о заметкой
        a_act = show_choose_user_actions(a_menu_list)  # Выведем меню для выбора режима работы
        if a_act == "0": # Быстрый выход
             exit()
        elif a_act == "1": # Режим редактирования заметки
            update_note(a_note, a_ind_of_note)   # Запускаем режим редактирования
        elif a_act == "2": # Режим работы со статусом заметки
            print(f"Статус текущей заметки - {a_note["4"]}.")
            a_note["4"] = status_change()
            a_notes = exchange_notes(a_note,a_ind_of_note) # Уточняем список с заметками
            save_notes(a_notes)
        elif a_act == "3":# Режим работы с датами заметки
            a_note = data_check(a_note)
        elif a_act == "4":# Режим работы с датами заметки
            a_note, a_ind_of_note = find_note(a_notes)
        else:
            print("Вы ввели некорректное число, режим не был активирован.")

    else:
        print("Вы ввели некорректное число, режим не был активирован.")

    a_ses_exit_allow = str(input("Продолжить работу в программе (нажмите ""1"") или выйти (любая другая)? > "))