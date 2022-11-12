'''
Описание игрока, его класс
'''

from ast import arg
import cursesmenu
from random import randint as rand


class Menu():
    def __init__(self) -> None:
        self.main_menu = cursesmenu.CursesMenu('Главное меню',
                    'Игра пиратская нажива',
                    show_exit_item=True
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
    def __init__(self, num):
        self.name = None
        self.__human = True
        self.__coins = 0 #  защита от читерства. Играйте честно.
        self.num = num
    
    def take_coin(self, num: int) -> str:
        if 0 < num <= 28:
            self.__coins += num
            turn_log = f'Вы забрали {num} монет'
        elif num <= 0:
            self.__coins += 1
            turn_log = '1 монета прилипла к вашим рукам'
        else:
            self.__coins += 28
            turn_log = f'К сожалению, {num - 28} монет не уместилось в руке и упали обратно.'
        return turn_log

    def get_player_coin_count(self):
        print(f'У игрока {self.name} сейчас {self.__coins} монет.')
        return self.__coins

    def create_player(self, name:str, human: bool):
        self.name = name
        self.__human = human


class Game(Menu):

    def __init__(self) -> None:
        super().__init__()
        self.__coins_count = 100
        self.set_game_mode()
        
    def show_menu(self):
        self.main_menu.start()
        self.main_menu.join()
    
    def set_game_mode(self):
        pvp_mode = cursesmenu.items.FunctionItem('Игрок против игрока',
                                                self.start_game, args=[2],
                                                should_exit=True
                                                )
        pve_mode = cursesmenu.items.FunctionItem('Игрок против компьютера',
                                                self.start_game, args=[1],
                                                should_exit=True
                                                )
        mode_menu = cursesmenu.CursesMenu('Выберите режим игры:')
        mode_menu.items.append(pvp_mode)
        mode_menu.items.append(pve_mode)
        mode_menu_item = cursesmenu.items.SubmenuItem('Начать игру', mode_menu,
                                                menu=self.main_menu,
                                                should_exit=True)
        self.main_menu.items.append(mode_menu_item)

    def start_game(self, player_count):
        self.player_1 = Player(1)
        self.player_2 = Player(2)
        if player_count == 2:
            self.player_1.create_player(name=input('Игрок 1 введите имя: '),
                                        human=True
                                        )
            self.player_2.create_player(name=input('Игрок 2 введите имя: '),
                                        human=True
                                        )
        else:
            self.player_1.create_player(name='Сильвер',
                                        human=True
                                        )
            self.player_2.create_player(name=input('Игрок 2 введите имя: '),
                                        human=False
                                        )
        order = self.toss_coin()
        self.game_menu = cursesmenu.CursesMenu('Пиратская доля', 
                                            f'',
                                            show_exit_item=True,
                                            )
        game_turn = cursesmenu.items.FunctionItem('Начать', 
                                                self.make_turn,
                                                args=[order, True],
                                                menu=self.game_menu
                                                )
        self.game_menu.items.append(game_turn)
        self.game_menu.start()
        self.main_menu.exit()

    def make_turn(self, first_step, start = False):
        order: int = first_step
        if order == 0:
            player = self.player_1
            order = 1
            next_player = self.player_2
        else:
            player = self.player_2
            order = 0
            next_player = self.player_1
        if self.__coins_count > 0:
            try:
                num = int(input(f'{player.name}, сколько монет вы кладете в руку?: '))
            except ValueError:
                print('Value err')
                num = 1
            log = self.take_coins(player, num)
            self.game_turn = cursesmenu.CursesMenu(f'{player.name} сделал ход. {log}', 
                                            f'В сундуке осталось {self.__coins_count} монеты',
                                            show_exit_item=False)
            next_turn = cursesmenu.items.FunctionItem(f'{next_player.name}, ваш ход',
                                                    self.make_turn,
                                                    args=[order])
            self.game_turn.items.append(next_turn)
            self.game_turn.start()
        else:
            self.end_game()
            return

    def end_game(self):
        self.game_menu.exit()
        self.main_menu.join()

    def go_to_main(self):
        self.game_menu.clear_screen()
        self.main_menu.show()
        self.main_menu.refresh_screen()

    def toss_coin(self):
        return 0 if rand(0,1) == 0 else 1

    def take_coins(self, player, num:int):
        if self.__coins_count - num >= 0 and 0 < num < 29:
            self.__coins_count -= num
        elif self.__coins_count > 0 and num == 0:
            self.__coins_count -= 1
        elif self.__coins_count - num >= 0 and num > 28:
            self.__coins_count -= 28
        else:
            print('error')
        return player.take_coin(num)
    
    def get_coins_balance(self):
        print(f'В сундуке осталось {self.__coins_count} монет')


if __name__=='__main__':
    game = Game()
    game.show_menu()
