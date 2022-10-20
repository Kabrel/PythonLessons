# -*- coding: utf8 -*-

"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

Так чтобы множетели не повторялись.
"""

number: int = int(input('Введите целое число: '))


def find_simple_divider(num: int) -> set[int]:
    result = set()
    if num % 2 == 0:
        result.add(2)
    for i in range(3, num + 1, 2):  # брать int(num ** 0.5) вместо num нельзя, ярко выражена ошибка на числах 33, 199
        while num % i == 0:
            result.add(i)
            num = num / i
    return result


print(', '.join([str(i) for i in find_simple_divider(number)]))
