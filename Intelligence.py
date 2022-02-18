from random import randint

class Intelligence():
    _OPTIMAL_TURN_SCORE = 17
    _MAX_TRUN_ROLL = 5
    
    _winner_score = 0
    _almost_win_score = 0
    
    def __init__(self, winner_score):
        self.winner_score = winner_score
        self.almost_win_score = winner_score -6
        
    def get_almost_win_score(self) -> int:
        return self.almost_win_score
    
    def should_roll(self, player_score, bot_score, turn_roll_num, turn_total_score) -> bool:
        """Determine whether it is optimal to roll again"""
        return not self.is_optimal_turn_score(turn_total_score) \
            or not self.is_max_turn_roll(turn_roll_num)
            
    def is_player_final_roll(self, player_score) -> bool:
        """Check if player can win in one roll"""
        return player_score >= self.get_almost_win_score()
    
    def is_bot_final_roll(self, turn_total_score, bot_score) -> bool:
        """Check if bot can win in one roll"""
        return (bot_score + turn_total_score) >= self.get_almost_win_score()
        
    def is_optimal_turn_score(self, turn_total_points) -> bool:
        """Check if total score for current turn is under optimal"""
        return turn_total_points >= self._OPTIMAL_TURN_SCORE
    
    def is_max_turn_roll(self, turn_roll_num) -> bool:
        """Check if number of rolls exceeds optimal number"""
        return turn_roll_num >= self._MAX_TRUN_ROLL
        
# "stand on 17" under certain circumstances,
# If you ask yourself how much you should risk, you need to know how much there is to gain. 
# Whenever your accumulated points are less than 20, you should continue throwing, because the odds are in your favor