from random import randint


class Dice:
    __turn_total_score = 0
    __turn_roll_num = 0

    def get_turn_roll_num(self):
        return self.__turn_roll_num

    def get_turn_total_score(self):
        return self.__turn_total_score

    def roll(self):
        points = randint(1, 6)
        if points == 1:
            self.reset_turn()
        else:
            self.__inc_turn_total_score(points)

        self.__inc_turn_roll_num()
        return points

    def reset_turn(self):
        self.__set_turn_total_score(0)
        self.__reset_turn_roll_num()
        return self

    def __set_turn_total_score(self, points):
        self.__turn_total_score = points

    def __inc_turn_total_score(self, add):
        self.__set_turn_total_score(self.get_turn_total_score() + add)

    def __inc_turn_roll_num(self):
        self.__turn_roll_num += 1

    def __reset_turn_roll_num(self):
        self.__turn_roll_num = 0
        return self
