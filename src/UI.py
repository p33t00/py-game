from cmd import Cmd
import os
from time import sleep
from typing import Callable
from lib.GUIHelper import GUIHelper

from src.Game import Game
from src.Dice import Dice
from src.Bot import Bot
from src.IntelligenceHigh import IntelligenceHigh
from src.Player import Player
from src.IntelligenceLow import IntelligenceLow


class UI(Cmd):
    __gui_helper = GUIHelper()
    __game = None
    __dice = None
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

    def do_start(self, arg):
        """Initializing the game"""
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
        """Reseting Bot"""
        self.reset_bot()
        self.do_start(arg)

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
        print(self.get_ghelper().get_intro())
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

    def get_ghelper(self):
        """GUIHelper getter"""
        return self.__gui_helper

    def get_intelligence(
        self, idx: int, win_score: int
    ) -> IntelligenceHigh or IntelligenceLow or False:
        """Get intalligence by index"""
        try:
            id = int(idx) - 1
            return self.__intelligence[id](win_score)
        except (ValueError, IndexError):
            return False

    def roll(self):
        """Roll action handler"""
        points = self.get_dice().roll()
        print(self.get_ghelper().get_picto_dice(points))
        if points == 1:
            self.do_stop("")

    def stop(self):
        """Stop action hanlder"""
        dice = self.get_dice()
        player = self.get_player()
        bot = self.get_bot()

        self.finalize_turn(player, dice)

        # Stopping the turn and pass it to next player
        print("Now it's Computer turn to roll...")
        bot.play(
            dice,
            player.get_total_points(),
            self.get_game().get_winner_score(),
            self.get_ghelper().get_picto_dice,
        )
        self.finalize_turn(bot, dice)

    def game_init_check(self, content: Callable):
        """Wrapper for action functionality that checks if game is initialized"""
        if self.get_game():
            content()
        else:
            print("Please start the game first")

    def init_bot(self):
        """Initialize Computer player"""
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

    def reset_bot(self):
        self.__bot = None

    def finalize_turn(self, participant, dice):
        """Finalize participant turn and display results"""
        new_total = participant.get_total_points() + dice.get_turn_total_score()
        print(f"{participant.get_name()} total score is {new_total}")

        self.process_turn_result(self.get_game(), dice, participant)

    def process_turn_result(self, game, dice, participant):
        """Processing and saving turn results"""
        if dice.get_turn_total_score() != 0:
            participant.add_points(dice.get_turn_total_score())
            dice.reset_turn()
            if game.has_won(participant.get_total_points()):
                self.cls()
                print(f"{participant.get_name()} is the winner !!!\n")
                self.get_ghelper().play_again(self.do_start, self.do_exit, self.cls)
