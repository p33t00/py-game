class Intelligence:
    __winner_score = 0

    def __init__(self, win_score):
        self.__winner_score = win_score

    def should_roll(
        self, player_score=0, bot_score=0, turn_total_score=0, turn_roll_num=0
    ) -> bool:
        pass

    def is_winner_score(self, score):
        return score >= self.__winner_score