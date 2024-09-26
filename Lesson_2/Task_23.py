"""Четкова Наталия
Задание 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict."""

a = int(input("Введите номер месяца в виде целого числа от 1 до 12 - "))
my_list = ['None', 'Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn', 'Autumn', 'Winter']
print(my_list[a])


my_dict = {1: "Spring", 2: "Summer", 3: "Autumn", 4: "Winter"}
if 2 < a < 6:
    i = 1
elif 5 < a < 9:
    i = 2
elif 8 < a < 12:
    i = 3
else:
    i = 4
print(my_dict.get(i))
