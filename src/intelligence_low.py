"""Robot intelligence Low module"""
from random import randint
from src.intelligence import Intelligence


class IntelligenceLow(Intelligence):
    """Bot intelligence implementation (Low)"""
    def should_roll(
        self, player_score=0, bot_score=0, turn_total_score=0, turn_roll_num=0
    ):
        return bool(randint(0, 1))
