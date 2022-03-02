"""Robot module."""
from time import sleep
from typing import Callable
from src.dice import Dice
from src.participant import Participant


class Bot(Participant):
    """Robot participant implementation."""

    __ghelper = None
    __intelect = None

    def __init__(self, name, intelect, gui):
        """Initialize class instance variables."""
        super().__init__(name)
        self.__intelect = intelect
        self.__ghelper = gui

    def get_intelect(self):
        """Intelect class getter."""
        return self.__intelect

    def get_ghelper(self):
        """Get GUIHelper."""
        return self.__ghelper

    def roll_again(
        self,
        player_score: int,
        bot_score: int,
        turn_total_score: int,
        turn_roll_num: int,
    ):
        """Roll again decision logic (roll or stop turn."""
        return self.get_intelect().should_roll(
            player_score, bot_score, turn_total_score, turn_roll_num
        )

    def play(self, dice: Dice, player_total: int, dice_visual: Callable, delay=1):
        """Bot playing."""
        while True:
            points = dice.roll()
            print(dice_visual(points))
            sleep(delay)
            if points == 1 or not self.roll_again(
                player_total,
                self.get_total_points(),
                dice.get_turn_total_score(),
                dice.get_turn_roll_num(),
            ):
                break
