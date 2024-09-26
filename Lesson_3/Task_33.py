"""Четкова Наталия
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""
def s_sum_max(var_1, var_2, var_3):
    if var_3 + var_2 > var_1 + var_3:
        if  var_3 + var_2 > var_2 + var_1:
            result = var_3 + var_2
    elif var_1 + var_2 > var_3 + var_2:
        if var_1 + var_2 > var_3 + var_1:
           result = var_1 + var_2
    else:
        result = var_1 + var_3
    return result

var_1 = int(input("Введите число - "))
var_2 = int(input("Введите число - "))
var_3 = int(input("Введите число - "))
print(s_sum_max(var_1, var_2, var_3))
