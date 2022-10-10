# -*- coding: utf8 -*-

"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""

input_a = input('Введите координаты точки А через запятую: ')
input_b = input('Введите координаты точки B через запятую: ')

while True:
    coordinate_a = input_a.split(',')
    coordinate_b = input_b.split(',')
    try:
        if len(coordinate_a) == 2 and len(coordinate_b) == 2:
            x_a = float(coordinate_a[0])
            y_a = float(coordinate_a[1])
            x_b = float(coordinate_b[0])
            y_b = float(coordinate_b[1])
            result = ((x_b - x_a)**2 + (y_b - y_a)**2)**0.5
            print("%.2f" % result)
            break
        else:
            print('Введены не верные данные_1.')
            break
    except ValueError:
        print('Введены не верные данные.')
        break
