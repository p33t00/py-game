"""Factory module for Intelligence."""
from src.intelligence import Intelligence
from src.intelligence_low import IntelligenceLow
from src.intelligence_high import IntelligenceHigh
from src.game import Game


class IntelligenceFactory:
    """Factory of Intelligence instance."""

    __game = None
    __intelligence = [IntelligenceLow, IntelligenceHigh]

    def __init__(self, game: Game):
        """Initialize instance."""
        self.__game = game

    def get_game(self):
        """Getter for Game."""
        return self.__game

    def get_intelligence(self, idx: int) -> Intelligence or False:
        """Get intelligence by index."""
        return self.__intelligence[idx](self.get_game())
