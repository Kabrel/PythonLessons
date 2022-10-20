# -*- coding: utf8 -*-

"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""
try:
    value = int(input('Введите целое число: '))
    result = ''
    if value == 0:
        print(0)
    else:
        while value >= 1:
            result = str(value % 2) + result
            value = value // 2
        print(result)
except ValueError:
    print('Введены не верные данные')

