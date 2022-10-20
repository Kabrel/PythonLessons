# -*- coding: utf8 -*-

"""
Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""
from decimal import Decimal
from math import pi

degree = int(input('Введите число от 1 до 10: '))

print(round(pi, Decimal(str(10**-degree)).as_tuple().exponent*(-1)))
