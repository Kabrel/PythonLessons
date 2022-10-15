# -*- coding: utf8 -*-

"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""

value = int(input('Введите целое число: '))
result = ''

while value >= 1:
    result = str(value % 2) + result
    value = value // 2
print(result)
