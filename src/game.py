"""Game module"""


class Game:
    """Game implementation"""
    __WINNER_SCORE = 100

    def get_winner_score(self):
        """__WINNER_SCORE getter"""
        return self.__WINNER_SCORE

    def has_won(self, participant_points):
        """Check if participant has enough points to win"""
        return participant_points >= self.__WINNER_SCORE
