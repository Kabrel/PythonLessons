
"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
"""
from os.path import exists as file_exists
from random import randint
import Task_3

file_count = 2

values_dict = {}

for i in range(1, file_count+1):
    if not file_exists(f"file_{i}"):
        with open(f'file_{i}', 'w') as f:
            data = Task_3.set_degree_values(10)
            f.write(data)
    with open(f'file_{i}', 'r') as f:
        for v in f:
            values_dict[f'val_{i}'] = v

print(values_dict)

value_1 = values_dict['val_1'].split(' + ') # генерировать словарь в зависимости от степени к
