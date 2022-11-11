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

import random as rnd
import keyboard

class Player():
    def __init__(self) -> None:
        self.name = None
        self.__human = True
        self.__coins = 0
    
    def take_coin(self, amount: int) -> str:
        if 0 < amount <= 28:
            self.__coins += amount
            turn_log = f'Вы забрали {amount} монет'
        elif amount <= 0:
            self.__coins += 1
            turn_log = '1 монета прилипла к вашим рукам'
        else:
            self.__coins += 28
            turn_log = f'К сожалению, {amount - 28} монет не уместилось в руке и упали обратно.'
        return turn_log
    
    def get_player_coin_amount(self):
        print(f'У игрока {self.name} сейчас {self.__coins} монет.')
        return self.__coins

    def create_player(self, name: str, is_human: bool):
        self.name = name
        self.__human = is_human

class Game():
    def __init__(self, balance) -> None:
        super().__init__()
        self.__coins_balance = balance
        self.__game_mode = None
        self.player_1 = Player()
        self.player_2 = Player()
        self.order = self.toss_coin()

    def set_game_mode(self, mode: int):
        if mode == 1:
            self.__game_mode = 'PvP'
            
        elif mode == 2:
            self.__game_mode = 'PvE'
    
    def toss_coin(self):
        return 1 if rnd.randint(0, 1) else 0

    def make_turn(self, player) -> str:
        print('')
        if self.__game_mode == 'PvP' or player.__human:
            try:
                num = int(input(f'{self.name}, сколько монет вы кладете в руку?: '))
            except ValueError:
                print('К сожалению удалось взять только одну монету')
                num = 1
        else:
            if 29 < self.__coins_balance < 58:
                num = self.__coins_balance - 29
            elif self.__coins_balance <= 28:
                num = self.__coins_balance
            else:
                num = rnd.randint(1, 28)
        log = self.take_coins()
        return log

    def take_coins(self, player, amount: int) -> str:
        if self.__coins_count - amount >= 0 and 0 < amount < 29:
            self.__coins_count -= amount
        elif self.__coins_count > 0 and amount == 0:
            self.__coins_count -= 1
        elif self.__coins_count - amount >= 0 and amount > 28:
            self.__coins_count -= 28
        else:
            print('error')
        return player.take_coin(amount)

    def get_coins_balance(self):
        print(f'В сундуке осталось {self.__coins_count} монет')

    def cls(self): 
            print("/n" * 100)

    def start(self):
        print('Пиратская доля')
        try:
            main_menu = int(input('Выберите пункт меню:\n'
                                '1 Правила\n'
                                '2 Старт игры\n'
                                '3 Выход'))
        except ValueError:
            self.cls()
            self.start()
        if main_menu == 1:
            self.cls()
            print('Правила:',
                'В сундуке лежит 2021 монета.\n' 
                'Играют два игрока делая ход друг после друга.' 
                'Первый ход определяется жеребьёвкой.' 
                'За один ход можно забрать не более чем 28 монет.\n' 
                'Все конфеты оппонента достаются сделавшему'
                'последний ход.'
                )
            print('нажмите ENTER для возврата назад')
            if keyboard.is_pressed('enter'):
                self.cls
                self.start()
        if main_menu == 2:
            self.cls()



        



        




