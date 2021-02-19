# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f_obj = open('hw5-1.txt', 'w', encoding='utf-8')

my_list = []
while True:
    line = input("Введите текст: ")
    if line == '':
        print(my_list)
        f_obj.writelines(my_list)
        f_obj.close()
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

