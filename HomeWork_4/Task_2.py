# -*- coding: utf8 -*-

"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""

number: int = int(input('Введите целое число: '))


def find_simple_divider(num: int) -> list[int]:
    result = []
    while num % 2 == 0:
        result.append(2)
        num = num / 2
    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            result.append(i)
            num = num / i
    if num > 2:
        result.append(2)
    return result


print(', '.join([str(i) for i in find_simple_divider(number)]))
