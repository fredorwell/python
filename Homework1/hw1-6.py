first_day = int(input('Введите результат пробежки в первый день: '))
result = int(input('Введите желаемый результат: '))
day = 1

if  first_day  >= result:
    print('Спортсмен бегает уже больше или столько же сколько хочет')
else:
    while first_day < result:
        first_day = first_day * 1.1
        day = day + 1
    print(f'Спортсмен добьется нужного результата на {day} день')
