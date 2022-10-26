'''
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. 
Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
'''

from random import randint as rand
from pick import pick
import Task_2_classes as game_c

pick_set = {'start_game': {'title': 'Выберите режим игры (нажмите пробел '
                                    'для выбора)',
                        'options': ['Против игрока', 'Против компьютера'],
                        'multiselect': False},
            'select_side': {'title': 'Выберите орел или решка'
                                     '(нажмите пробел для выбора)',
                            'options': ['Орел', 'Решка'],
                            'multiselect': False},
            }


def create_player():
    p_name = input('Как вас зовут пират?: ')
    if p_name:
        return game_c.Player(p_name)
    else:
        return game_c.Player('Немой')


def create_bot():
    return game_c.Player('Сильвер', human=False)


def toss_coin():
    return "Орел" if rand(0,1) == 1 else "Решка"


def make_human_turn(player):
    while True:
        try:
            num = int(input('Сколько монет вы кладете в руку?: '))
            game_c.Game.take_coins(num)
            player.take_coin(num)
            break # продумать отрицательное количество монет
        except ValueError:
            pass


def make_bot_turn():
    pass


def start_game():
    print('Game started')
    players_count = pick(pick_set['start_game']['options'],
                         pick_set['start_game']['title'],
                         multiselect=pick_set['start_game']['multiselect']
                        )
    Player_1 = create_player()
    if players_count == 'Против игрока':
        Player_2 = create_player()
    else:
        Player_2 = create_bot()
    p_choose = pick(pick_set['select_side']['options'],
                    pick_set['select_side']['title'],
                    multiselect=pick_set['select_side']['multiselect']
                    )
    toss_coin()


start_game()
