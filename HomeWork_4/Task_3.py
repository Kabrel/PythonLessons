"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
и записать в файл многочлен степени k.

Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""

from random import randint

uni_dict = {"0": "\u2070",
                "1": "\u00B9",
                "2": "\u00B2",
                "3": "\u00B3",
                "4": "\u2074",
                "5": "\u2075",
                "6": "\u2076",
                "7": "\u2077",
                "8": "\u2078",
                "9": "\u2079",
                "-": "\u207B"
                }


def get_random_value(val):
    return tuple([randint(0, 100), val])


def make_unicode_number(data):
    result = ''.join(str(uni_dict[i]) for i in str(data))
    return result


def make_string(degree, val, k):
    exp = make_unicode_number(degree)  # Если функция раскоментирована, будет красивый текст.
    if degree == k:
        if val > 1:
            return f'{val}*x{exp}'
        else:
            return f'x{exp}'
    elif degree > 1:
        if val > 1:
            return f'{val}*x{exp}'
        elif val == 1:
            return f'x{exp}'
    elif degree == 1:
        if val > 1:
            return f'{val}*x'
        elif val == 1:
            return 'x'
    else:
        return f'{val}'


def set_degree_values(exp):
    result = ' + '.join([make_string(i, v, exp) for v, i in map(get_random_value, range(exp, -1, -1))])
    print(result + ' = 0')
    return result
