"""GUIHelper module."""
from pathlib import Path


class GUIHelper:
    """GUI Helper class."""

    __picto_dice = ()

    def __init__(self) -> None:
        self.__load_picto_dice()

    def get_intro(self) -> str:
        """Return intro ASCII Picture."""
        return Path("assets/intro.txt").read_text("UTF8")

    def get_rules(self):
        """Return game rules."""
        return Path("assets/rules_n_instruct.txt").read_text("UTF8")

    def play_again(self) -> bool:
        """Asks if player wants to play again."""
        while True:
            resp = input("Play again ?\n (y/n):\n")
            if resp == "y":
                return True
            elif resp == "n":
                return False
            else:
                print("Invalid input. Please try again.")

    def get_picto_dice(self, idx):
        """Return visual representation of dice in plain text."""
        return self.__picto_dice[idx - 1]

    def __load_picto_dice(self):
        """Load visual representation of dice."""
        self.__picto_dice = Path("assets/picto-dice.txt").read_text().split("\n\n")
