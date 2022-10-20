
"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
и записать в файл многочлен степени k.

Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""

from random import randint

k = int(input('Введите целое число > 1: '))


def get_random_value(val):
    return tuple([randint(0, 100), val])


'''
По какой то причине, на машине не работает юникод

def make_unicode_number(data):
    print(str(data))
    uni_dict = {"0": u"\u2070",
                "1": u"\u00B9",
                "2": u"\u00B2",
                "3": u"\u00B3",
                "4": u"\u2074",
                "5": u"\u2075",
                "6": u"\u2076",
                "7": u"\u2077",
                "8": u"\u2078",
                "9": u"\u2079",
                "-": u"\u207B"
                }
    result = ''.join(str(uni_dict[i]) for i in str(data))
    return result
'''


def make_string(degree, val):
    try:
        exp = make_unicode_number(degree)  # Если функция раскоментирована, будет красивый текст.
    except:
        exp = degree
    if degree == k:
        if val > 1:
            return f'{val}*x**{exp}'
        else:
            return f'x**{exp}'
    elif degree > 1:
        if val > 1:
            return f'{val}*x**{exp}'
        elif val == 1:
            return f'x**{exp}'
    elif degree == 1:
        if val > 1:
            return f'{val}*x'
        elif val == 1:
            return 'x'
    else:
        return f'{val}'


def set_degree_values(exp):
    result = ' + '.join([make_string(i, v) for v, i in map(get_random_value, range(exp, -1, -1))])
    print(result + ' = 0')


set_degree_values(k)
