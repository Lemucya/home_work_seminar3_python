"""
1) Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""

def calculator(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f'Ошибка!!! Делить на ноль нельзя!')

print(calculator(int(input('Введите делимое а: ')),
                 int(input('Введите делитель b: '))))

"""
вариант преподавателя:

def division(first_obj, second_obj):
    try:
        return first_obj/second_obj
    except ZeroDivisionError:
        return "Пытаетесь делить на 0!"

try:
    first_numb = int(input("Введите первое число: "))
    second_numb = int(input("Введите второе число: "))
    print(division(first_numb, second_numb))
except ValueError:
    print("Пожалуйста, вводите только числа")
"""