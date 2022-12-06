"""
6) Реализовать функцию int_func(), принимающую слово из маленьких латинских
букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(words):
    return ' '.join(s[:1].upper() + s[1:] for s in words.split(' '))


text = input("Введите слово или строку для преобразования:\n")
print(int_func(text))


"""
вариант преподавателя:

# часть 1
def int_func(string):
    return string.title()
    
print(int_func("text"))

# часть 2
def title_func(string):
    list_title = []
    lst = string.split()
    for el in lst:
        list_title.append(int_func(el))
        
    print(*list_title)
    
title_func("каждое слово теперь с заглавной буквы")
"""