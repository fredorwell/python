# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.


summa = 0
count = 0
employess = []

with open("hw5-3.txt", "r") as file_obj:

    for line in file_obj:
        print(line, end="")

        employee = line.split('-')

        if int(employee[1]) <= 20000:
            employess.append(employee[0])
        summa += int(employee[1])
        count += 1

print(f"Сотрудники с зп ниже 20к: {employess}")


result = summa / count
print(f"Средняя зп всех сотрудников: {result}")

