"""
3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    print(
        f'Сумма двух наибольших аргументов равна: '
        f'{arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(
    int(input('Аргумент 1: ')),
    int(input('Аргумент 2: ')),
    int(input('Аргумент 3: ')),
)

"""
вариант преподавателя:

Вариант 1
def get_max(*args):
    print(sum(sorted(list(args), reverse=True)[:2]))
    
get_max(100, 1, 200)

Вариант 2
def get_max(*args):
    lst = list(args)
    i = 0
    res = 0
    while i != 2:
        max_val = max(lst)
        res += max_val
        lst.remove(max_val)
        i += 1
    print(res)
    
get_max(100, 1, 200)
"""