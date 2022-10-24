'''
Описание игрока, его класс
'''


class Game():

    def __init__(self):
        self.__coins_count = 2021

    def take_coins(self, num:int):
        if 0 < num <= 28:
            self.__coins_count -= num
        elif num == 0:
            self.__coins_count -= 1
        else:
            self.__coins_count -= 28
    
    def get_coins_balance(self):
        print(f'В сундуке осталось {self.__coins_count} монет')


class Player():
    def __init__(self, name = 'Player', human=True):
        self.name = name
        self.__human = human
        self.__coins = 0 #  защита от читерства. Играйте честно.
    
    def take_coin(self, num: int):
        if 0 < num <= 28:
            self.__coins += num
        elif num == 0:
            self.__coins += 1
            print('1 монета прилипла к вашим рукам')
        else:
            self.__coins += 28
            print(f'К сожалению, {num - 28} монет не уместилось в руке и упали обратно.')
    
    def get_player_coin_count(self):
        print(f'У игрока {self.name} сейчас {self.__coins} монет.')
        return self.__coins


new_game = Game()