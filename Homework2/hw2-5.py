# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
# элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.


user_element = int(input("Введите число: "))
l = [7, 5, 3, 3, 2]


c = l.count(user_element)
for element in l:

    if c > 0:
        i = l.index(user_element)
        l.insert(i + c, user_element)

        break
    else:

        if user_element > element:
            j = l.index(element)
            l.insert(j, user_element)
            break

        elif user_element < l[len(l) - 1]:
            l.append(user_element)

print(l)
