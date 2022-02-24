class Game:
    __WINNER_SCORE = 100

    def get_winner_score(self):
        return self.__WINNER_SCORE

    def has_won(self, participant_points):
        return participant_points >= self.__WINNER_SCORE
