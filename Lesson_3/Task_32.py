"""Четкова Наталия
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""

def s_dates(name, surname, year_of_birth, city_of_residence, email, phone):
    return (f"Name - {name}; surname - {surname}; year_of_birth - {year_of_birth}; city_of_residence - {city_of_residence}; email - {email}; phone - {phone}")

name = input("Enter name - ")
surname = input("Enter surname - ")
year_of_birth = input("Enter year of birth - ")
city_of_residence = input("Enter city of residence - ")
email = input("Enter email - ")
phone = input("Enter phone - ")

print(s_dates(name.title(), surname.title(), year_of_birth, city_of_residence.title(), email, phone))
