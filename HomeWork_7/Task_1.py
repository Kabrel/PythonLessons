#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

под форматами понимаем структуру файлов, например: в файле на одной строке хранится одна часть записи,
пустая строка - разделитель

Фамилия_1
Имя_1
Телефон_1
Описание_1

Фамилия_2
Имя_2
Телефон_2
Описание_2

и т.д. в файле на одной строке хранится все записи, символ разделитель -;

Фамилия_1,Имя_1,Телефон_1,Описание_1
Фамилия_2,Имя_2,Телефон_2,Описание_2
и т.д.

Можно явно указать на использование CSV
Если группа сильная, можно предложить внедрить JSON, XML
"""

from Task_1_funcs import *
from random import randint

user_dict = {0: {'name': '',
                 'surname': '',
                 'tel': '',
                 'description': '',
                 },
             }


def cls():  # clear console
    return '\n' * 100


def main_menu():
    while True:
        try:
            print()
            choice = int(input('Выберите пункт меню:\n1) Записать пользователя\n2) Импортировать данные из файла\n3) '
                               'Экспортировать данные в файл\n4) Поиск пользователей\n5) Выход\n'))
            break
        except ValueError:
            print('Данный пункт меню не существует')
    if choice == 1:  # Record user
        while True:
            user_id = randint(1, 1000)
            if not user_dict.get(user_id):
                user_dict[user_id] = add_record()
                print('Запись добавлена')
                save_data(user_dict)
                return main_menu()
            else:
                pass
    elif choice == 2:  # Import data
        f_name = input('Введите название файла: ')
        import_data(f_name)
        print('Файл импортирован')
        return main_menu()
    elif choice == 3:  # Export data
        f_name = input('Введите название файла: ')
        export_data(f_name)
        print('Файл экспортирован')
        return main_menu()
    elif choice == 4:  # Search info
        user_search = input('Введите данные для поиска: ')
        search_info(user_dict, user_search)
        return main_menu()
    elif choice == 5:  # Exit
        return


if __name__ == '__main__':
    main_menu()
