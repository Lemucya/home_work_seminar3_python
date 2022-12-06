"""
4) Программа принимает действительное положительное число x и целое
отрицательное число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y). При решении
задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в
степень с помощью оператора *.
Второй — более сложная реализация без оператора *, предусматривающая
использование цикла.
"""


def my_abs(x):
    return x if x >= 0 else x * -1


def raising_to_power(x, y):
    result = x
    for i in range(my_abs(y) - 1):
        result *= x
    if y < 0:
        result = 1 / result
    return result


try:
    basis = int(input("Введите положительное число x = "))
    degree = int(input("Введите отрицательное число y = "))
    print(f"x ** y =  {raising_to_power(basis, degree)}")
except ValueError as e:
    print(e)

"""
вариант преподавателя:

try:
    if y < 0:
        res = 1
        for i in range(y, 0):
            res = res * x
        res = 1 / res
        return f'Для значений х = {5}, у = {-3} результат: {res}'
        
    else:
        return "Число у должно быть строго отрицательным"
        
    except TypeError:
        return "Пожалуйста, вводите только числа"
    except ZeroDivisionError:
        return "На ноль делить нельзя"
        
print(get_val(5, -3))
"""