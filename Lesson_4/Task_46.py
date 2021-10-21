"""Четкова Наталия
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""

from itertools import count
from itertools import cycle

for el in count(10.0, 1.0):
    if el > 1000:
        break
    else:
        print(el)


my_list = [1, 1, 2, 7, 3, 27, 1, 55, 55, 57, 1, 2, 10, 7, 4, 111]
c = 0
for el in cycle(my_list):
    if c > 30:
        break
    print(el)
    c += 1
