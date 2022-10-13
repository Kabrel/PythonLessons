# -*- coding: utf8 -*-

"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
"""
import random

n_count = int(input('Введите количество элементов: '))
index_list = range(1, n_count+1)

val_dict = {str(key): random.randint(-n_count, n_count) for key in index_list}

[print(f'Позиция {k}: значение {v}') for k, v in val_dict.items()]

with open('file.txt', "w") as f:
    for i in index_list:
        f.write(str(i) + '\n')

with open('file.txt', 'r') as f:
    positions = random.sample([i.replace('\n', '') for i in f], 2)

print(f'Позиции для перемножения {positions[0]} и {positions[1]}')

result = val_dict[positions[0]] * val_dict[positions[1]]
print('Результат =', result)
