
"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
"""
from os.path import exists as file_exists
from random import randint
import Task_3

file_count = 2

values_dict = {}


def check_all_condition(v_data):
    print(v_data)\
    if len(v_data) > 1:
        if not v_data[1][1:]:
            return '1', v_data[0]
        else:
            return v_data[1][1:], v_data[0]
    else:
        return '0', v_data[0]



def add_data_to_dict(val: list):
    print(check_all_condition(val))



for i in range(1, file_count+1):
    if not file_exists(f"file_{i}"): #  создаем файл, если его нет и заполняем его данными
        with open(f'file_{i}', 'w') as f:
            data = Task_3.set_degree_values(10)
            f.write(data)
    with open(f'file_{i}', 'r') as f:
        for v in f:
            for elements in v.split(' + '): #  разделяем многочлены на отдельные элементы.
                values = elements.split('*')
                add_data_to_dict(values)
                        #values_dict['1']

            #if values_dict.get()

print(values_dict)


