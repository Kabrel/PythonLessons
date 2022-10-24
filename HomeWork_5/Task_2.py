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
import Task_2_classes as game


def create_player():
    p_name = input('Как вас зовут пират?: ')
    if p_name:
        return game.Player(p_name)
    else:
        return game.Player('Немой')


def create_bot():
    return game.Player('Сильвер', human=False)


def toss_coin():
    return "Орел" if rand(0,1) == 1 else "Решка"


def make_human_turn(player):
    while True:
        try:
            num = int(input('Сколько монет вы кладете в руку?: '))
            game.Game.take_coins(num)
            player.take_coin(num)
            break # продумать отрицательное количество монет
        except ValueError:
            pass

def make_bot_turn():
    pass

def start_game():
    players_count = int(print('Введите кол-во игроков (1 или 2): '))
    Player_1 = create_player()
    if players_count >= 2:
        Player_2 = create_player()
    else:
        Player_2 = create_bot()
    p_choose = input()
    toss_coin()
