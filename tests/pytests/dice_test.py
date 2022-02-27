import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from src.dice import Dice


class TestDice:
    def test_get_turn_roll_num(self, dice):
        assert(dice.get_turn_roll_num() == 0)
        dice._Dice__inc_turn_roll_num()
        assert(dice.get_turn_roll_num() == 1)
        dice._Dice__inc_turn_roll_num()
        assert(dice.get_turn_roll_num() == 2)
        dice._Dice__inc_turn_roll_num()
        assert(dice.get_turn_roll_num() == 3)

    def test_get_turn_total_score(self, dice):
        assert dice.get_turn_total_score() == 0
        dice._Dice__inc_turn_total_score(15)
        assert(dice.get_turn_total_score() == 15)
        dice._Dice__inc_turn_total_score(8)
        assert(dice.get_turn_total_score() == 23)

    @pytest.mark.parametrize('execution_number', range(3))
    def test_roll(self, dice, execution_number):
        rng = range(1, 7)
        points = dice.roll()
        assert(points in rng)
        points = dice.roll()
        assert(points in rng)
        points = dice.roll()
        assert(points in rng)

    def test_reset_turn(self, dice):
        for i in range(5):
            dice.roll()
            dice.reset_turn()
            assert(dice.get_turn_roll_num() == 0)
            assert(dice.get_turn_total_score() == 0)

    @pytest.fixture(scope="function")
    def dice(self):
        return Dice()
