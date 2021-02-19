# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка:
# [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.


import json

with open('hw5-7.txt', 'r', encoding='utf-8') as f_txt:
    lines = f_txt.readlines()

firm_dict = {}
average_profit = []


for line in lines:
    firm_name, firm_form, firm_revenue, firm_cost = line.split()
    firm_profit = int(firm_revenue) - int(firm_cost)
    if firm_profit > 0:
        average_profit.append(firm_profit)
    firm_dict[firm_name] = firm_profit


average_profit = sum(average_profit) / len(average_profit)
# print(firm_dict)
# print(average_profit)
summary_data = [firm_dict, {'Средний доход' : round(average_profit)}]
print(summary_data)

with open('hw5-7.json', 'w+') as f_json:
    json.dump(summary_data, f_json)

with open('hw5-7.json') as f_json:
    print(json.load(f_json))

