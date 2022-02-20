class IntelligenceAdvanced():
    _optimal_turn_score = 17
    _max_turn_roll = 5
    
    _winner_score = 0
    _almost_win_score = 0
    
    def __init__(self, winner_score):
        self.winner_score = winner_score
        self.almost_win_score = winner_score -10    
        
    def get_almost_win_score(self) -> int:
        return self.almost_win_score
    
    def get_optimal_turn_score(self):
        return self._optimal_turn_score
    
    def get_max_turn_roll(self):
        return self._max_turn_roll
    
    def should_roll(self, player_score, bot_score, turn_total_score, turn_roll_num) -> bool:
        """Determine whether it is optimal to roll again"""
        return self.is_player_final_roll(player_score) \
            or self.is_bot_final_roll(turn_total_score, bot_score) \
            or not self.is_max_turn_roll(turn_roll_num) \
            or not self.is_optimal_turn_score(turn_total_score)
            
    def is_player_final_roll(self, player_score) -> bool:
        """Check if player can win in one roll"""
        return player_score >= self.get_almost_win_score()
    
    def is_bot_final_roll(self, turn_total_score, bot_score) -> bool:
        """Check if bot can win in one roll"""
        return (bot_score + turn_total_score) >= self.get_almost_win_score()
        
    def is_optimal_turn_score(self, turn_total_points) -> bool:
        """Check if total score for current turn is under optimal"""
        return turn_total_points >= self.get_optimal_turn_score()
    
    def is_max_turn_roll(self, turn_roll_num) -> bool:
        """Check if number of rolls exceeds optimal number"""
        return turn_roll_num > self.get_max_turn_roll()