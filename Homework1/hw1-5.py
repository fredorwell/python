# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceed = int(input('Введите сумму выручки: '))
cost = int(input('Введите сумму расходов: '))
total = proceed - cost
if total < 0:
    print(f' Компания работает с убытком: {total} ')
elif 0 == total:
    print(' Компания работает в ноль')
else:
    empl = int(input('Введите количество сотрудников: '))
    print(f'Прибыль на одного сотрудника: {total / empl}')
