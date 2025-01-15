title_list = [] # Задание массива (списка)
title_count = 3 # Задание числа заголовков
for i in range(0, title_count): # Цикл ввода и помещения в список заголовков
    title = input("Введите заголовок заметки №" + str(i+1)+ ": ")
    title_list.append(title)
# print("Перечень заголовков:", title_list) # Краткий формат вывода

# Подробный вывод
print(f"Cписок заголовков заметки: "
      f"первый - {title_list[0]}, "
      f"второй - {title_list[1]}, "
      f"третий - {title_list[2]}.")
