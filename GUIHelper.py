from inspect import _void
from pathlib import Path
from typing import Callable


class GUIHelper:
    __picto_dice = ()

    def __init__(self) -> None:
        self.load_picto_dice()

    def get_intro(self) -> str:
        '''Return intro ASCII Picture'''
        return Path("intro.txt").read_text()

    def play_again(
        self, y_callb: Callable, n_callb: Callable, else_callb: Callable
    ) -> _void:
        """Asks if player wants to play again"""
        while True:
            resp = input("Play again ?\n (y/n):\n")
            if resp == "y":
                y_callb(None)
                break
            elif resp == "n":
                n_callb(None)
                break
            else:
                else_callb()
                print("Invalid input. Please try again.")

    def get_picto_dice(self, idx):
        """Returns visual representation of dice in plain text"""
        try:
            return self.__picto_dice[idx - 1]
        except IndexError:
            return "X"

    def load_picto_dice(self):
        """Loads visual representation of dice"""
        self.__picto_dice = Path("picto-dice.txt").read_text().split("\n\n")
