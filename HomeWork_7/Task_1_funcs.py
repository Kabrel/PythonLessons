#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Функции для записи, экспорта и поиска данных по базе.
"""
import json


def add_record():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    tel = input('Введите телефон: ')
    description = input('Введите описание: ')
    return {'name': name, 'surname': surname, 'tel': tel, 'description': description}


def save_data(data: dict):
    with open('db.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data))


def import_data(f_name):
    f_type = f_name.split('.')[-1]
    with open(f_name, 'r', encoding='utf-8') as f:
        if f_type == 'json':
            return json.loads(f.read())
        elif f_type == 'xml':
            pass
        elif f_type == 'txt':
            pass


def export_data(f_name):
    f_type = f_name.split('.')[-1]
    data = {}
    with open('db.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    with open(f_name, 'x', encoding='utf-8') as f:
        if f_type == 'json':
            f.write(json.dumps(data))
        elif f_type == 'xml:':
            pass
        elif f_type == 'txt':
            pass


def search_info(data, param):
    for value in data.values():
        for item in value.values():
            if item == param:
                print(f'Имя: {item["name"]}')
                print(f'Фамилия: {item["surname"]}')
                print(f'Телефон: {item["tel"]}')
                print(f'Описание: {item["description"]}')
            else:
                print('Таких пользователей не найдено.')
