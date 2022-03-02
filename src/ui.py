"""UI module."""
from cmd import Cmd
import sys
import os
from time import sleep
from typing import Callable

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../lib/"))
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../lib/intelligence/"))

from src.game import Game
from src.dice import Dice
from src.bot import Bot
from src.player import Player
from src.highScore import HighScore
from gui_helper import GUIHelper
from intelligence_factory import IntelligenceFactory


class UI(Cmd):
    """Implementation of UI actions."""

    __gui_helper = GUIHelper()
    __game = None
    __dice = None
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

    def do_start(self, arg):  # pylint: disable=W0613
        """Initialize the game."""
        self.__game = Game()
        self.__dice = Dice()

        if self.get_player():
            self.get_player().reset_total_points()
        else:
            self.__player = Player(input("Enter your name: "))

        if self.get_bot():
            self.get_bot().reset_total_points()
        else:
            self.__bot = self.__get_init_bot()

        self.cls()
        print("Lets Begin !")

    def do_restart(self, arg):  # pylint: disable=W0613
        """Restarting the game."""
        self.__game_init_check(lambda: self.do_start(""))

    def do_reset_bot(self, arg):  # pylint: disable=W0613
        """Reset Bot."""
        self.__reset_bot()
        self.do_start(arg)

    def do_cheat(self, arg):
        """Multiplying Player's roll result by provided value."""
        self.__game_init_check(lambda: self.__cheat(arg))

    def do_roll(self, arg):  # pylint: disable=W0613
        """Roll dice."""
        self.__game_init_check(self.__roll)

    def do_stop(self, arg):  # pylint: disable=W0613
        """Stop player turn and passing it to Bot."""
        self.__game_init_check(self.__stop)

    def do_exit(self, arg):  # pylint: disable=W0613
        """Exit game."""
        print("Good game, see ya next time !")
        sleep(2)
        self.cls()
        exit()  # pylint: disable=R1722

    def cls(self):
        """Clear the screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def preloop(self):
        """Initialize game app."""
        self.cls()
        print(self.get_ghelper().get_intro())
        sleep(2)
        self.cls()
        print(self.get_ghelper().get_rules())
        # return super().preloop()

    def precmd(self, line) -> any:
        """Run before every command."""
        self.cls()
        return line

    def get_game(self):
        """Game getter."""
        return self.__game

    def get_dice(self):
        """Dice getter."""
        return self.__dice

    def get_bot(self):
        """Bot getter."""
        return self.__bot

    def get_player(self):
        """Player getter."""
        return self.__player

    def get_ghelper(self):
        """GUIHelper getter."""
        return self.__gui_helper

    def __roll(self):
        """Roll action handler."""
        points = self.get_dice().roll()
        print(self.get_ghelper().get_picto_dice(points))
        if points == 1:
            self.do_stop("")

    def __stop(self):
        """Stop action hanlder."""
        dice = self.get_dice()
        player = self.get_player()
        bot = self.get_bot()

        if not self.__process_and_continue(player):
            return

        # Stopping the turn and pass it to next player
        print("Now it's Computer turn to roll...")
        bot.play(
            dice,
            player.get_total_points(),
            self.get_ghelper().get_picto_dice,
        )
        self.__process_and_continue(bot)

    def __cheat(self, arg):
        """Cheat action handler."""
        try:
            self.get_player().set_cheat_rate(int(arg))
            print(f"Cheat x{arg} is activated :D")
            sleep(2)
            self.cls()
        except (TypeError, ValueError):
            print("Something went wrong. Try again with different input")

    def __game_init_check(self, content: Callable):
        """Check if game is initialized. Wrapper for UI actions."""
        if self.get_game():
            content()
        else:
            print("Please start the game first")

    def __get_init_bot(self):
        """Initialize and return Computer player."""
        print("Select Bot intelligence level:", "1. Low", "2. High", sep="\n", end="\n")
        iq_factory = IntelligenceFactory(self.get_game())
        intelligence_id = self.get_ghelper().get_intelect_id()
        intelligence = iq_factory.get_intelligence(intelligence_id - 1)
        return Bot("Computer", intelligence, self.get_ghelper())

    def __reset_bot(self):
        """Reset Bot participant."""
        self.__bot = None

    def __process_and_continue(self, participant) -> bool:
        """Process and save turn results."""
        participant.add_points(self.get_dice().get_turn_total_score())
        self.get_dice().reset_turn()
        if self.get_game().has_won(participant.get_total_points()):
            self.__game_over_handler(participant)
            return False
        print(
            f"{participant.get_name()} total score is {participant.get_total_points()}"
        )
        return True

    def __game_over_handler(self, participant):
        """Finalize the game."""
        self.cls()
        print(f"{participant.get_name()} is the winner !!!\n")
        print(f"You have scored {self.__player.get_total_points()} points.\n")
        self.scoreboard()
        if self.get_ghelper().play_again():
            self.cls()
            self.do_start("")
        else:
            self.cls()
            self.do_exit("")

    def scoreboard(self):
        """Store all scores and display top 5."""
        HighScore.store_score_in_dict(HighScore, self.__player.get_name(), self.__player.get_total_points())
        HighScore.display_scoreboard(HighScore)
