# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

my_range = range(20, 241)
new_list = [element for element in my_range if element%20==0 or element%21==0]
print(new_list) 