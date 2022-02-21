from Participant import Participant


class Bot(Participant):
    intelect = None

    def __init__(self, name, intelect):
        super().__init__(name)
        self.intelect = intelect

    def roll_again(self, player_score, bot_score, turn_total_score, turn_roll_num):
        return self.intelect.should_roll(
            player_score, bot_score, turn_total_score, turn_roll_num
        )
