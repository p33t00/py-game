import random
from Participant import Participant

class Bot(Participant):
    # def __init__(self, intelect):
    #     self.intelect = intelect
        
    def level_advanced(self):
        # 'if toss = small point -> toss more times'
        # 'if toss = large point -> toss less times'
        # 'if got too far in points from player than can stop'
        pass
    
    def roll_again(self):
        'implement intellect usage here'
        # stop more often ON EASY level
        return bool(random.randint(0,1))