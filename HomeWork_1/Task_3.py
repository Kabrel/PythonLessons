# -*- coding: utf8 -*-

"""
3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""

while True:
    value_x = input('Ввведите координаты точки x: ')
    value_y = input('Ввведите координаты точки y: ')
    try:
        x = float(value_x)
        y = float(value_y)
        if x > 0 and y > 0:
            quarter = 1
        elif x > 0 and y < 0:
            quarter = 2
        elif x < 0 and y < 0:
            quarter = 3
        elif x < 0 and y > 0:
            quarter = 4
        else:
            print('Лежит на оси координат')
            break
        print(f"x = {x} и y = {y}, принадлежат {quarter} четверти")
        break
    except ValueError:
        print('Введите правильные данные.')
