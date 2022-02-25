"""Participant module"""


class Participant:
    """Implementation of Participant (init class for participants)"""
    _total_points = 0
    _name = ""

    def __init__(self, name="default"):
        self._name = name

    def get_total_points(self):
        """__total_points getter"""
        return self._total_points

    def get_name(self):
        """__name getter"""
        return self._name

    def reset_total_points(self):
        """Reset of __total_points"""
        self._total_points = 0

    def add_points(self, points):
        """Adding points to participant score"""
        self._total_points += points

    def set_name(self, name):
        """___name setter"""
        self._name = name
