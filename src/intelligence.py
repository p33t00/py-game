"""Robot intelligence module"""
from abc import ABC, abstractmethod


class Intelligence(ABC):
    """Initial class for Bot intelligence"""
    __winner_score = 0

    def __init__(self, win_score: int):
        self.__winner_score = win_score

    @abstractmethod
    def should_roll(
        self, player_score, bot_score, turn_total_score, turn_roll_num
    ) -> bool:  # pragma: no cover
        """Method that will contain logic which will determine if turn should be stopped"""

    def is_winner_score(self, score) -> int:  # pragma: no cover
        """Check if provided score reached winner score"""
        return score >= self.__winner_score
