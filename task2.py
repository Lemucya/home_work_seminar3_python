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

"""
вариант преподавателя:

def user_info(name, surname, year_of_birth, city, email, phone):
    print(f"{name} {surname} {year_of_birth} года рождения," 
        f"проживает в городе {city}, email: {email}, телефон: {phone}")
        
user_info(
    name="Иван",
    surname="Иванов",
    year_of_birth="1846",
    city="Москва",
    email="jackie@gmail.com",
    phone="01005321456"
)
"""
