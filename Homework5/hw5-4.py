# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translater = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
result = []
f_obj = open("hw5-4.txt", 'r', encoding='utf-8')


for line in f_obj:
    split_line = line.split(" — ")
    if split_line[0] in translater:
        word = translater[split_line[0]]
        result.append(word +' - '+ split_line[1])


print(result)
f_obj_translate = open("hw5-4-tr.txt", 'w', encoding='utf-8')
f_obj_translate.writelines(result)