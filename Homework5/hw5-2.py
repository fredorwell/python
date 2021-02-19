# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

f_obj = open('hw5-2.txt', 'r', encoding='utf-8')

lines = 0
letters = 0

for line in f_obj:
    lines += line.count("\n")
    letters = len(line) - 1
    print(f"в строке {lines} - {letters} букв ")

