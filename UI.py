from cmd import Cmd
from pathlib import Path
import os
from time import sleep
from typing import Callable

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

        if self.get_player():
            self.get_player().reset_total_points()
        else:
            self.__player = Player(input("Enter your name: "))

        if self.get_bot():
            self.get_bot().reset_total_points()
        else:
            self.init_bot()

        print("Lets Begin !")

    def do_restart(self, arg):
        """Restarting the game"""
        self.game_init_check(lambda: self.do_start(arg))

    def do_reset_bot(self, arg):
        """Reseting Bot intelligence"""
        self.game_init_check(self.init_bot)

    def do_roll(self, arg):
        """Rolling dice"""
        self.game_init_check(self.roll)

    def do_stop(self, arg):
        """Stopping player turn and passing it to Bot"""
        self.game_init_check(self.stop)

    def do_exit(self, arg) -> bool:
        """Exit game"""
        print("Good game, see ya next time !")
        sleep(2)
        self.cls()
        exit()

    def cls(self):
        """Clearing the screen"""
        os.system("cls" if os.name == "nt" else "clear")

    def preloop(self) -> None:
        """Initializing game app"""
        self.cls()
        print(Path("intro.txt").read_text())
        self.load_picto_dice()
        sleep(2)
        self.cls()
        return super().preloop()

    def precmd(self, line) -> any:
        """Run before every command"""
        self.cls()
        return line

    def get_game(self):
        """Game getter"""
        return self.__game

    def get_dice(self):
        """Dice getter"""
        return self.__dice

    def get_bot(self):
        """Bot getter"""
        return self.__bot

    def get_player(self):
        """Player getter"""
        return self.__player

    def get_intelligence(
        self, idx: int, win_score: int
    ) -> IntelligenceHigh or IntelligenceLow:
        """Get intalligence by index"""
        try:
            id = int(idx) - 1
            return self.__intelligence[id](win_score)
        except (ValueError, IndexError):
            return False

    def roll(self):
        points = self.get_dice().roll()
        print(self.get_picto_dice(points))
        if points == 1:
            self.do_stop("")

    def stop(self):
        dice = self.get_dice()
        player = self.get_player()
        bot = self.get_bot()

        self.finalize_turn(player, dice)

        # Stopping the turn and pass it to next player
        print("Now it's Computer turn to roll...")
        self.bot_play(
            dice, bot, player.get_total_points(), self.get_game().get_winner_score()
        )
        self.finalize_turn(bot, dice)

    def game_init_check(self, content: Callable):
        """Wrapper for action functionality that checks if game is initialized"""
        if self.get_game():
            content()
        else:
            print("Please start the game first")

    def init_bot(self):
        print("Select Bot intelligence level:", "1. Low", "2. High", sep="\n", end="\n")
        while True:
            intelligence = self.get_intelligence(
                input(), self.get_game().get_winner_score()
            )
            if intelligence:
                break
            else:
                print("Invalid index. Please try again: ")

        self.__bot = Bot("Computer", intelligence)

    # refactor method args and usage
    def bot_play(self, dice, bot, player_total, win_score):
        """Bot playing its\' turn"""
        while True:
            points = dice.roll()
            print(self.get_picto_dice(points))
            sleep(1)
            if points == 1 or not bot.roll_again(
                player_total,
                bot.get_total_points(),
                dice.get_turn_total_score(),
                win_score,
            ):
                break

    def finalize_turn(self, participant, dice):
        self.print_new_total(
            participant.get_name,
            participant.get_total_points() + dice.get_turn_total_score(),
        )
        self.process_turn_result(self.get_game(), dice, participant)

    def process_turn_result(self, game, dice, participant):
        """Functionality to finalize participant\'s turn"""
        if dice.get_turn_total_score() != 0:
            participant.add_points(dice.get_turn_total_score())
            dice.reset_turn()
            if game.has_won(participant.get_total_points()):
                self.cls()
                print(f"{participant.get_name()} is the winner !!!\n")
                self.play_again()

    def play_again(self):
        """Asks if player wants to play again"""
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

    def print_new_total(self, participant_name, total_score):
        print(f"{participant_name()} total score is {total_score}")

    def get_picto_dice(self, idx):
        """Returns visual representation of dice in plain text"""
        try:
            return self.__picto_dice[idx - 1]
        except IndexError:
            return False

    def load_picto_dice(self):
        """Loads visual representation of dice"""
        self.__picto_dice = Path("picto-dice.txt").read_text().split("\n\n")
