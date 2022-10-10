# -*- coding: utf8 -*-

"""
4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
 в этой четверти (x и y).
"""

value_quarter = input('Введите номер четверти от 1 до 4: ')

quarter_dict = {'1': '0 < x < inf, 0 < y < inf',
                '2': '0 < x < inf, -inf < y < 0',
                '3': '-inf < x < 0, -inf < y < 0',
                '4': '-inf < x < 0, 0 < y < inf'
                }

if value_quarter in quarter_dict.keys():
    print(f'Возможные значения координат для данной четверти: {quarter_dict[value_quarter]}')
else:
    print('Введены не коректные данные')
