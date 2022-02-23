from cmd import Cmd
from pathlib import Path
import os
from posixpath import split
from time import sleep

from pkg_resources import split_sections
from Game import Game
from Dice import Dice
from Bot import Bot
from IntelligenceHigh import IntelligenceHigh
from Player import Player
from IntelligenceLow import IntelligenceLow


class UI(Cmd):
    __game = None
    __dice = None
    __bot = None
    __player = None
    __intelligence = [IntelligenceLow, IntelligenceHigh]
    __picto_dice = ()
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
        self.__dice = Dice()
        self.__player = Player(input("Enter your name: "))

        print("Select Bot intelligence level:", "1. Low", "2. High", sep="\n", end="\n")
        intelligence = self.get_intelligence(
            int(input()) - 1, self.get_game().get_winner_score()
        )
        self.__bot = Bot("Computer", intelligence)

        print("Lets Begin !")

    # TODO: this method
    def do_restart(self, arg):
        self.do_start(arg)

    def do_roll(self, arg):
        if not self.get_game():
            self.do_start(arg)
        points = self.get_dice().roll()
        # print(f"you got {points}")
        print(self.get_picto_dice(points))
        if points == 1:
            self.do_stop("")

    def do_stop(self, arg):
        dice = self.get_dice()
        player = self.get_player()
        bot = self.get_bot()

        self.finalize_turn(self.get_game(), dice, player)

        # Stopping the turn and pass it to next player
        print("Now it's Computer turn to roll...")
        self.bot_play(
            dice, bot, player.get_total_points(), self.get_game().get_winner_score()
        )
        self.finalize_turn(self.get_game(), dice, bot)

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
        self.load_picto_dice()
        sleep(2)
        self.cls()
        return super().preloop()

    def precmd(self, line) -> any:
        self.cls()
        return line

    def get_game(self):
        return self.__game

    def get_dice(self):
        return self.__dice

    def get_bot(self):
        return self.__bot

    def get_player(self):
        return self.__player

    # refactor this. maybe __intelligence will not be needed
    def get_intelligence(
        self, idx: int, win_score: int
    ) -> IntelligenceHigh or IntelligenceLow:
        try:
            return self.__intelligence[idx](win_score)
        except IndexError:
            return self.get_intelligence(
                int(input("Invalid index. Please try again: ")) - 1, win_score
            )

    # refactor method args and usage
    def bot_play(self, dice, bot, player_total, win_score):
        while True:
            points = dice.roll()
            # print(f"Computer got {points}")
            print(self.get_picto_dice(points))
            sleep(1)
            if points == 1 or not bot.roll_again(
                player_total,
                bot.get_total_points(),
                dice.get_turn_total_score(),
                win_score,
            ):
                break

    # thonk over this method
    def finalize_turn(self, game, dice, participant):
        new_total = participant.get_total_points() + dice.get_turn_total_score()
        print(f"{participant.get_name()} total score is {new_total}")
        
        if dice.get_turn_total_score() == 0:
            return
        participant.add_points(dice.get_turn_total_score())
        if game.has_won(participant.get_total_points()):
            self.game_over(participant.get_name())
        dice.reset_turn()

    def game_over(self, participant_name):
        self.cls()
        print(f"{participant_name} is the winner !!!")
        self.get_bot().reset_total_points()
        self.get_player().reset_total_points()
        self.play_again()

    def play_again(self):
        while True:
            resp = input("Play again ?\n (y/n):\n")
            if resp == "y":
                self.do_start(None)
                break
            elif resp == "n":
                self.do_exit(None)
                break
            else:
                self.cls()
                print("Invalid input. Please try again.")

    def get_picto_dice(self, idx):
        try:
            return self.__picto_dice[idx-1]
        except IndexError:
            return False
    
    def load_picto_dice(self):
        self.__picto_dice = Path("picto-dice.txt").read_text().split('\n\n')
