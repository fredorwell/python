# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


f_obj = open("hw5-5.txt", 'w+', encoding='utf-8')
input_lines = input('Введите цифры через пробел ')
f_obj.writelines(input_lines)
split_lines = input_lines.split()
print(sum(map(int, split_lines)))
