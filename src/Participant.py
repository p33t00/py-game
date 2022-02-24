class Participant:
    __total_points = 0
    __name = ''

    def __init__(self, name='default'):
        self.__name = name

    def get_total_points(self):
        return self.__total_points

    def get_name(self):
        return self.__name

    def reset_total_points(self):
        self.__total_points = 0

    def add_points(self, points):
        self.__total_points += points

    def set_name(self, name):
        self.__name = name
