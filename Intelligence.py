from abc import ABC, abstractmethod


class Intelligence(ABC):
    __winner_score = 0

    def __init__(self, win_score: int):
        self.__winner_score = win_score

    @abstractmethod
    def should_roll(
        self, player_score=0, bot_score=0, turn_total_score=0, turn_roll_num=0
    ) -> bool:  # pragma: no cover
        pass

    def is_winner_score(self, score) -> int:  # pragma: no cover
        return score >= self.__winner_score
