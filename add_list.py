title_list = []
title_count = 3
for i in range(0, title_count):
    title = input("Введите заголовок заметки №" + str(i+1)+ ": ")
    title_list.append(title)
print("Перечень заголовков:", title_list)
