"""
2) Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def personal_data(name, surname, birth_year, city, email, phone):
    return print(f'{name} {surname}, {birth_year}, {city}, {email}, {phone}')


print("Введите следующую информацию: ")
personal_data(
    name=input('Имя: '),
    surname=input('Фамилия: '),
    birth_year=input('Год рождения: '),
    city=input('Город проживания: '),
    email=input('Email: '),
    phone=input('Телефон: '), )
