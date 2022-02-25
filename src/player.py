"""Player module"""
from src.participant import Participant


class Player(Participant):
    """Player implementation"""
    __cheat_rate = 1

    def get_cheat_rate(self):
        return self.__cheat_rate

    def set_cheat_rate(self, rate: int):
        self.__cheat_rate = rate if rate > 0 else 1

    def add_points(self, points: int):
        """Adding points to participant score"""
        self._total_points += (points * self.get_cheat_rate())
