# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n)
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from math import factorial

# def my_gen(number):
#     count = 1
#     while count <= number:
#         yield factorial(number)
# i = 1
# my_fifteen = []
# for el in my_gen(5):
#     if i > 15:
#         break
#     else:
#         my_fifteen.append(el)
#         i += 1
# print(my_fifteen)


from itertools import count
def fibo_gen():
    for el in count(1):  # бесконечный цикл, который начинается с 1
        yield factorial(el)

for step, i in enumerate(fibo_gen(), start=1):
    print(f"Факториал {step} - {i}")
    if step == 15:
        break

# Сдался на этой задаче, по этому просто разобрал ваше решение