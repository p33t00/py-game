from random import randint

# turn toggler
# introduce Rules (print)
# check if result is 1 or not
# roll result (print)
# start Game (scores = 0, )
# ? how to determine who rolls first ?
# maybe first roll will determine?
# if odd - bot, if even - player

# cheat functionality (multiplying roll results by 30)

# create Bot for the game with intelligence level selected by user


class Game:
    # TODO : CHECK HOW CONSTANTS ARE DEFINED
    __WINNER_SCORE = 100
    __turn_total_score = 0

    def get_turn_total_score(self):
        return self.__turn_total_score

    def set_turn_total_score(self, points):
        self.__turn_total_score = points

    def inc_turn_total_score(self, add):
        self.set_turn_total_score(self.get_turn_total_score() + add)
        return self.get_turn_total_score()

    def reset_turn_total_score(self):
        self.set_turn_total_score(0)

    def roll_dice(self):
        points = randint(1, 6)
        if points == 1:
            self.reset_turn_total_score()
        else:
            self.inc_turn_total_score(points)
        return points

    def stop(self, participant):
        participant.add_points(self.get_turn_total_score())
        self.reset_turn_total_score()

    def has_won(self, participant):
        return participant.get_total_points() >= self.__WINNER_SCORE
