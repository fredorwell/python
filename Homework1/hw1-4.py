# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

user_value = int(input('Введите большое число: '))
b = user_value % 10
user_value = user_value // 10
while user_value > 0:
    if user_value % 10 > b:
        b = user_value % 10
    user_value = user_value // 10

print(f' Самая большая цифра в числе: {b} ')

