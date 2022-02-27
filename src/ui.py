"""UI module"""
from cmd import Cmd
import os
from time import sleep
from typing import Callable
from lib.guiHelper import GUIHelper

from src.game import Game
from src.dice import Dice
from src.bot import Bot
from src.intelligence_high import IntelligenceHigh
from src.player import Player
from src.intelligence_low import IntelligenceLow


class UI(Cmd):
    """Implementation of UI actions"""
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

    def do_start(self, arg):  # pylint: disable=W0613
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
            self.__init_bot()

        print("Lets Begin !")

    def do_restart(self, arg):  # pylint: disable=W0613
        """Restarting the game"""
        self.__game_init_check(lambda: self.do_start(''))

    def do_reset_bot(self, arg):  # pylint: disable=W0613
        """Reseting Bot"""
        self.__reset_bot()
        self.do_start(arg)

    def do_cheat(self, arg):
        """Multiplying Player's roll result by provided value"""
        self.__game_init_check(lambda: self.__cheat(arg))

    def do_roll(self, arg):  # pylint: disable=W0613
        """Rolling dice"""
        self.__game_init_check(self.__roll)

    def do_stop(self, arg):  # pylint: disable=W0613
        """Stopping player turn and passing it to Bot"""
        self.__game_init_check(self.__stop)

    def do_exit(self, arg):  # pylint: disable=W0613
        """Exit game"""
        print("Good game, see ya next time !")
        sleep(2)
        self.cls()
        exit()  # pylint: disable=R1722

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
            decr_id = int(idx) - 1
            return self.__intelligence[decr_id](win_score)
        except (ValueError, IndexError):
            return False

    def __roll(self):
        """Roll action handler"""
        points = self.get_dice().roll()
        print(self.get_ghelper().get_picto_dice(points))
        if points == 1:
            self.do_stop('')

    def __stop(self):
        """Stop action hanlder"""
        game = self.get_game()
        dice = self.get_dice()
        player = self.get_player()
        bot = self.get_bot()

        if not self.__process_and_continue(game, player, dice):
            return

        # Stopping the turn and pass it to next player
        print("Now it's Computer turn to roll...")
        bot.play(
            dice,
            player.get_total_points(),
            game.get_winner_score(),
            self.get_ghelper().get_picto_dice,
        )
        self.__process_and_continue(game, bot, dice)

    def __cheat(self, arg):
        """Cheat action handler"""
        try:
            self.get_player().set_cheat_rate(int(arg))
            print(f"Cheat x{arg} is activated :D")
            sleep(2)
            self.cls()
        except TypeError:
            print("Something went wrong. Try again with other input")

    def __game_init_check(self, content: Callable):
        """Wrapper for action functionality that checks if game is initialized"""
        if self.get_game():
            content()
        else:
            print("Please start the game first")

    def __init_bot(self):
        """Initialize Computer player"""
        print("Select Bot intelligence level:", "1. Low", "2. High", sep="\n", end="\n")
        while True:
            intelligence = self.get_intelligence(
                input(), self.get_game().get_winner_score()
            )
            if intelligence:
                break
            print("Invalid index. Please try again: ")

        self.__bot = Bot("Computer", intelligence)

    def __reset_bot(self):
        """Reseting Bot participant"""
        self.__bot = None

    def __process_and_continue(self, game, participant, dice) -> bool:
        """Processing and saving turn results"""
        participant.add_points(dice.get_turn_total_score())
        dice.reset_turn()
        if game.has_won(participant.get_total_points()):
            self.cls()
            print(f"{participant.get_name()} is the winner !!!\n")
            if self.get_ghelper().play_again():
                self.cls()
                self.do_start("")
            else:
                self.cls()
                self.do_exit("")
            return False

        print(f"{participant.get_name()} total score is {participant.get_total_points()}")
        return True
