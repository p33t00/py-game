from cmd import Cmd
from pathlib import Path
import os
from time import sleep
from Game import Game
from Bot import Bot
from IntelligenceHigh import IntelligenceHigh
from Player import Player
from IntelligenceLow import IntelligenceLow


class UI(Cmd):
    __game = None
    __bot = None
    __player = None
    __intelligence = [IntelligenceLow, IntelligenceHigh]
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
        self.__player = Player(input("Enter your name: "))

        print("Select Bot intelligence level:", "1. Low", "2. High", sep="\n", end="\n")
        intelligence = self.get_intelligence(int(input()) - 1, self.get_game().get_winner_score())
        self.__bot = Bot("Computer", intelligence)

        print("Lets Begin !")

    def do_restart(self, arg):
        self.do_start(arg)

    def do_roll(self, arg):
        if not self.get_game():
            self.do_start(arg)
            
        points = self.get_game().roll_dice()
        print(f"you got {points}")
        if points == 1:
            self.do_stop("")

    def do_stop(self, arg):
        player = self.get_player()
        player.add_points(self.__game.get_turn_total_score())
        print(f"{player.get_name()} score is {player.get_total_points()}")
        if self.__game.has_won(player):
            self.game_over(player)
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
            roll_again = bot.roll_again(
                player.get_total_points(),
                bot.get_total_points(),
                self.get_game().get_turn_total_score(),
                self.get_game().get_winner_score())

        bot.add_points(self.get_game().get_turn_total_score() * 20)
        print(f"{bot.get_name()} score is {bot.get_total_points()}")
        if self.__game.has_won(bot):
            self.game_over(bot)
            return
        self.__game.reset_turn_total_score()

    def do_quit(self, arg) -> bool:
        """Alias for "exit" command"""
        return self.do_exit(arg)

    def do_exit(self, arg) -> bool:
        """Exit this game"""
        print("Good game, see ya next time !")
        sleep(2)
        self.cls()
        exit()

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

    def get_intelligence(self, idx: int, win_score: int) -> IntelligenceHigh or IntelligenceLow:
        try:
            return self.__intelligence[idx](win_score)
        except IndexError:
            return self.get_intelligence(int(input("Invalid index. Please try again: ")) - 1,
                                         win_score)

    def game_over(self, player):
        self.cls()
        print(f"{player.get_name()} is the winner !!!")
        self.get_bot().reset_total_points()
        self.get_player().reset_total_points()
        self.get_game().reset_turn_roll_num().reset_turn_total_score()
        self.play_again()

    def play_again(self):
        while True:
            resp = input('Play again ?\n (y/n)')
            if resp == 'y':
                self.do_start(None)
                break
            elif resp == 'n':
                self.do_exit(None)
                break
            else:
                self.cls()
                print('Invalid input. Please try again.')
