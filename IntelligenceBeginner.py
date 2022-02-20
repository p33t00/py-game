from random import randint

class IntelligenceBeginner:
    def should_roll(self, player_score, bot_score, turn_total_score, turn_roll_num):
        return bool(randint(0,1))