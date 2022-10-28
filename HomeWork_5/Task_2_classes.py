'''
Описание игрока, его класс
'''
from turtle import screensize
import cursesmenu


class Menu():
    def __init__(self) -> None:
        self.main_menu = cursesmenu.CursesMenu('Главное меню',
                    'Игра пиратская нажива'
                    )
        self.set_rules()
        
    def set_rules(self): #  необходимо поправить отображение многострочного кода
        self.__rules = cursesmenu.CursesMenu('Правила:',
                    'В сундуке лежит 2021 монета.\n' 
                    'Играют два игрока делая ход друг после друга.' 
                    'Первый ход определяется жеребьёвкой.' 
                    'За один ход можно забрать не более чем 28 монет.\n' 
                    'Все конфеты оппонента достаются сделавшему'
                    'последний ход.'
                    )
        rules_menu = cursesmenu.items.SubmenuItem('Правила',
                                                self.__rules,
                                                self.main_menu
                                                )
        self.main_menu.items.append(rules_menu)


class Player():
    def __init__(self):
        self.name = None
        self.__human = True
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

    def create_player(self, name:str, human: bool):
        self.name = name
        self.__human = human


class Game(Menu, Player):

    def __init__(self) -> None:
        super().__init__()
        self.__coins_count = 2021
        self.set_game_mode()
        self.main_menu.show()
        
    def set_game_mode(self):
        pvp_mode = cursesmenu.items.FunctionItem('Игрок против игрока',
                                                self.start_game, args=[2]
                                                )
        pve_mode = cursesmenu.items.FunctionItem('Игрок против компьютера',
                                                self.start_game, args=[1]
                                                )
        mode_menu = cursesmenu.CursesMenu('Выберите режим игры:')
        mode_menu.items.append(pvp_mode)
        mode_menu.items.append(pve_mode)
        mode_menu_item = cursesmenu.items.SubmenuItem('Начать игру', mode_menu,
                                                menu=self.main_menu)
        self.main_menu.items.append(mode_menu_item)

    def start_game(self, player_count):
        pass

    def take_coins(self, num:int):
        if 0 < num <= 28:
            self.__coins_count -= num
        elif num == 0:
            self.__coins_count -= 1
        else:
            self.__coins_count -= 28
    
    def get_coins_balance(self):
        print(f'В сундуке осталось {self.__coins_count} монет')

if __name__=='__main__':
    Game()
