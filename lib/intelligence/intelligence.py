"""Robot intelligence module."""
from abc import ABC, abstractmethod


class Intelligence(ABC):
    """Initial class for Bot intelligence."""

    __game = None

    def __init__(self, game: int):
        """Initialize instance variables."""
        self.__game = game

    def get_game(self):
        """Game getter."""
        return self.__game

    @abstractmethod
    def should_roll(
        self, player_score, bot_score, turn_total_score, turn_roll_num
    ) -> bool:  # pragma: no cover
        """Check if should roll again.

        Method that will contain logic which will determine if turn should be stopped.
        """

    def is_winner_score(self, score) -> int:  # pragma: no cover
        """Check if provided score reached winner score."""
        return self.get_game().has_won(score)
