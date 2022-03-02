"""Robot intelligence High module."""
from intelligence import Intelligence


class IntelligenceHigh(Intelligence):
    """Bot intelligence implementation (High)."""

    __optimal_turn_score = 14
    __max_turn_roll = 5

    __almost_win_score = 0

    def __init__(self, game):
        """Initialize instance variables."""
        super().__init__(game)
        self.__almost_win_score = game.get_winner_score() - 10

    def get_almost_win_score(self) -> int:
        """win_score getter."""
        return self.__almost_win_score

    def get_optimal_turn_score(self):
        """optimal_turn_score getter."""
        return self.__optimal_turn_score

    def get_max_turn_roll(self):
        """max_turn_roll getter."""
        return self.__max_turn_roll

    def should_roll(
        self, player_score, bot_score, turn_total_score, turn_roll_num
    ) -> bool:
        """Determine whether it is optimal to roll again."""
        if self.is_winner_score(turn_total_score + bot_score):
            return False

        if self.is_player_final_turn(player_score):
            return True

        if self.is_bot_final_turn(turn_total_score, bot_score):
            return True

        if self.is_optimal_turn_score(turn_total_score):
            return False

        if self.is_max_turn_roll(turn_roll_num):
            return False

        return True

    def is_player_final_turn(self, player_score) -> bool:
        """Check if player can win in one turn."""
        return player_score >= self.get_almost_win_score()

    def is_bot_final_turn(self, turn_total_score, bot_score) -> bool:
        """Check if bot can win in one turn."""
        return (bot_score + turn_total_score) >= self.get_almost_win_score()

    def is_optimal_turn_score(self, turn_total_points) -> bool:
        """Check if total score for current turn is under optimal."""
        return turn_total_points >= self.get_optimal_turn_score()

    def is_max_turn_roll(self, turn_roll_num) -> bool:
        """Check if number of rolls exceeds optimal number."""
        return turn_roll_num > self.get_max_turn_roll()
