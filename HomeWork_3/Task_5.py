# -*- coding: utf8 -*-

"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

num = int(input('Введите целое число: '))

fib = [0, 1]
result = []
for i, v in enumerate(fib):
    if i < num - 1:
        fib.append(fib[i]+fib[i+1])
    else:
        break
neg_fib = [-i ** -i for i in fib if i != 0]
result = fib.extend(neg_fib)
print(sorted(fib))
# советую проверять на числе 300, получается красивый рисунок
