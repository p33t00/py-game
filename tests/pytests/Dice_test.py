import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from src.Dice import Dice


class TestGame:
    def test_get_inc_turn_roll_num(self, dice):
        """Testing get_turn_roll_num() & inc_turn_roll_num() methods"""
        assert dice.get_turn_roll_num() == 0
        dice.inc_turn_roll_num()
        assert dice.get_turn_roll_num() == 1
        dice.inc_turn_roll_num()
        assert dice.get_turn_roll_num() == 2
        dice.inc_turn_roll_num()
        assert dice.get_turn_roll_num() == 3

    def test_get_set_turn_total_score(self, dice):
        """Testing get_turn_total_score() & set_turn_total_score()"""
        assert dice.get_turn_total_score() == 0
        dice.set_turn_total_score(30)
        assert dice.get_turn_total_score() == 30

    def test_inc_turn_total_score(self, dice):
        assert dice.get_turn_total_score() == 0
        dice.inc_turn_total_score(15)
        assert dice.get_turn_total_score() == 15
        dice.inc_turn_total_score(6)
        assert dice.get_turn_total_score() == 21
        
    def test_reset_turn_roll_num(self, dice):
        assert dice.get_turn_total_score() == 0
        dice.inc_turn_total_score(15)
        dice.
        assert dice.get_turn_total_score() == 0
        dice.inc_turn_total_score(10)
        dice.inc_turn_total_score(8)
        assert dice.get_turn_total_score() == 0
        

    @pytest.fixture(scope="function", autouse=True)
    def dice(self):
        return Dice()
