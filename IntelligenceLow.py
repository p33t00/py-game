from random import randint


class IntelligenceLow:
    def should_roll(
        self, player_score=0, bot_score=0, turn_total_score=0, turn_roll_num=0
    ):
        return bool(randint(0, 1))
