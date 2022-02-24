from time import sleep
from typing import Callable
from src.Dice import Dice
from src.Participant import Participant
from lib.GUIHelper import GUIHelper


class Bot(Participant):
    __ghelper = GUIHelper()
    __intelect = None

    def __init__(self, name, intelect):
        super().__init__(name)
        self.__intelect = intelect

    def get_ghelper(self):
        return self.__ghelper

    def roll_again(self, player_score: int, bot_score: int, turn_total_score: int, turn_roll_num: int):
        return self.__intelect.should_roll(
            player_score, bot_score, turn_total_score, turn_roll_num
        )

    def play(self, dice: Dice, player_total: int, win_score: int, dice_visual: Callable):
        """Bot playing its\' turn"""
        while True:
            points = dice.roll()
            print(dice_visual(points))
            sleep(1)
            if points == 1 or not self.roll_again(
                player_total,
                self.get_total_points(),
                dice.get_turn_total_score(),
                win_score,
            ):
                break
