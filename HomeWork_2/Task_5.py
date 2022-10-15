# -*- coding: utf8 -*-

"""
Реализуйте алгоритм перемешивания списка.
"""

from random import random

data = [i for i in input('введите данные: ')]
print(data)
print(sorted(data, key=lambda i: random()))
