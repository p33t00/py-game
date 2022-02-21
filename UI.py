from cmd import Cmd
from pathlib import Path
import os
from time import sleep
from Game import Game
from Bot import Bot
from Player import Player
from IntelligenceLow import IntelligenceLow


class UI(Cmd):
    __game = None
    __bot = None
    __player = None
    # intro = Path('intro.txt').read_text()
    # intro = '''
    # ------------------------
    # | Welcome... PIGGY !!! |
    # ------------------------
    # '''

    prompt = "<(PiG)> "
    file = None
    # doc_header = 'doc_header'
    # misc_header = 'misc_header'
    # undoc_header = 'undoc_header'
    # identchars = '123456789'

    # ruler = '='

    # TODO: make restart game
    def do_start(self, arg):
        "Initializing the game"
        self.__game = Game()
        self.__bot = Bot("Computer", IntelligenceLow())
        self.__player = Player("Pete")
        print("Lets Begin !")

    def do_roll(self, arg):
        points = self.get_game().roll_dice()
        print(f"you got {points}")
        if points == 1:
            self.do_stop("")

    # TODO: handle "empty" stop commands
    def do_stop(self, arg):
        player = self.get_player()
        player.add_points(self.__game.get_turn_total_score())
        print(f"{player.get_name()} score is {player.get_total_points()}")
        if self.__game.has_won(player):
            print("You are the winner !!!")
            return
        self.__game.reset_turn_total_score()

        "Stopping the turn and pass it to next player"
        print("Now it's Computer turn to roll...")
        points = 0
        roll_again = True
        bot = self.get_bot()
        while roll_again and points != 1:
            points = self.get_game().roll_dice()
            print(f"Computer got {points}")
            sleep(1)
            roll_again = bot.roll_again(0, 0, 0, 0)

        bot.add_points(self.__game.get_turn_total_score())
        print(f"{bot.get_name()} score is {bot.get_total_points()}")
        if self.__game.has_won(player):
            print(f"{bot.get_name} is the winner !!!")
            return
        self.__game.reset_turn_total_score()

    def do_quit(self, arg) -> bool:
        'Alias for "exit" command'
        return self.do_exit(arg)

    def do_exit(self, arg) -> bool:
        "Exit this game"
        print("Good game, see ya next time !")
        sleep(2)
        self.cls()
        return True

    def cls(self):
        os.system("cls" if os.name == "nt" else "clear")

    def preloop(self) -> None:
        self.cls()
        print(Path("intro.txt").read_text())
        sleep(2)
        self.cls()
        return super().preloop()

    def precmd(self, line) -> any:
        self.cls()
        return line

    def get_game(self):
        return self.__game

    def get_bot(self):
        return self.__bot

    def get_player(self):
        return self.__player
