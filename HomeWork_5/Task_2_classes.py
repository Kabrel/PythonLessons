'''
Описание игрока, его класс
'''


class Player():
    def __init__(self, name = 'Player'):
        self.name = name
        self.__coins = 0 #  защита от читерства. Играйте честно.
    
    def take_coin(self, num: int):
        if num <= 28:
            self.__coins += num
        else:
            self.__coins += 28
            print(f'К сожалению, {num - 28} монет не уместилось в руке и упали обратно.')
    
    def get_coin_count(self):
        print(f'У игрока {self.name} сейчас {self.__coins} монет.')
