# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_str = input("Введите строку: ")
user_str_split = user_str.split()
print(user_str_split)
for i, element in enumerate(user_str_split, 1):
    if len(element) > 10:
        element = element[0:10]
    print(f"{i}. - {element}")