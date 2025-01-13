# Полный код по спецификации с активной частью по спецификации № 1.4 по Grade 1:
#username = input("Введите имя пользователя")
title_list = []
title_count = 3
for i in range(0, title_count):
    title = input("Введите заголовок заметки №" + str(i+1)+ ": ")
    title_list.append(title)
#content = input("Введите саму заметку")
#status = input("Укажите статус заметки")
#created_date = input("Введите дату создания")
#issue_date = input("Введите дату (срок) выполнения")
#print("Имя пользователя:", username)
print("Перечень заголовков:", title_list)
#print("Содержимое:", content)
#print("Статус заметки:", status)
#print("Сокр. дата создания:",created_date[0:5])
#print("Сокр. дата выполнения:", issue_date[0:5])