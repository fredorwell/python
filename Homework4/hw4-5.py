# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
def my_func(prev_element, element):
    return prev_element * element

my_list = [element for element in range(100, 1001) if element % 2 == 0]
print(reduce(my_func, my_list))

