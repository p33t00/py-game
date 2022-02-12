from random import randint

class Intelligence():
    def get_logic_simple(self, player_score, bot_score, roll_in_turn_num) -> bool:
        return bool(randint(0,1))
    
    def get_logic_difficult(self, player_score, bot_score, roll_in_turn_num, turn_total_points) -> bool:
        pass
        # chck if average score for this turn is high (turn_total > roll_in_turn_num * 4,5,6)
        
    def is_low_avg_turn_score(turn_total_points) -> bool:
        turn_total_points * 16.1 
        
# "stand on 17" under certain circumstances,
# If you ask yourself how much you should risk, you need to know how much there is to gain. 
# Whenever your accumulated points are less than 20, you should continue throwing, because the odds are in your favor