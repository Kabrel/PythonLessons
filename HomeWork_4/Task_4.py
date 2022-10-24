
"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
"""
from os.path import exists as file_exists
from random import randint
import Task_3

values_dict = {}


def make_number_from_unicode(num):
    inv_dict = {v: k for k, v in Task_3.uni_dict.items()}
    result = ''.join(str(inv_dict[i]) for i in str(num))
    return result


def check_all_condition(v_data):
    result = None
    if len(v_data) > 1:
        if not v_data[1][1:]:
            result = ('1', v_data[0])
        else:
            result =  (make_number_from_unicode(v_data[1][1:]), v_data[0])
    else:
        result =  ('0', v_data[0])
    return result


def add_data_to_dict(val: list):
    key = int(check_all_condition(val)[0])
    item = int(check_all_condition(val)[1])
    if not values_dict.get(key):
        values_dict[key] = item
    else:
        values_dict[key] += item


def make_polynomial(data, biggest_x):
    '''
    начиная с питона 3.7 словари стали упорядоченными, 
    поэтому порядок задан при создании словаря.
    '''
    polynomial = ' + '.join([Task_3.make_string(i,v,biggest_x) for i, v in data.items()])
    return polynomial

def run_app(file_count, count=10):
    for i in range(1, file_count+1):
        if not file_exists(f"file_{i}"): #  создаем файл, если его нет и заполняем его данными
            with open(f'file_{i}', 'w') as f:
                data = Task_3.set_degree_values(count)
                f.write(data)
        with open(f'file_{i}', 'r') as f:
            for v in f:
                for elements in v.split(' + '): #  разделяем многочлены на отдельные элементы.
                    values = elements.split('*')
                    add_data_to_dict(values)
    result = make_polynomial(values_dict, count)
    print(result, '= 0')
    return result


run_app(2, 10)
