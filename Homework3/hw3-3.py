# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(x, y, z):
    inp_num = [x, y, z]
    max_list = []
    max1 = max(inp_num)
    max_list.append(max1)
    inp_num.remove(max1)
    max2 = max(inp_num)
    max_list.append(max2)
    print(sum(max_list))


my_func(10, 5, -10)

