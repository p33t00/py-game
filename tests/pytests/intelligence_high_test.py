import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from src.game import Game
from src.intelligence import Intelligence
from src.intelligence_high import IntelligenceHigh


class TestIntelligenceHigh:
    def test_is_intelligence_cls(self):
        assert issubclass(IntelligenceHigh, Intelligence)

    """player_score, bot_score, turn_total_score, turn_roll_num"""
    @pytest.mark.parametrize(
        "should_roll_args",
        [
            [0, 0, 0, 0, True],  # beginning of the game
            [87, 91, 3, 3, True],  # bot last roll
            [98, 81, 3, 3, True],  # player last roll
            [37, 29, 18, 3, False],  # optimal turn score
            [87, 79, 10, 5, True],  # max turn roll score
            [37, 29, 26, 7, False],  # finish turn
            [77, 87, 18, 3, False],  # winning score
        ],
    )
    def test_should_roll(self, intelligence, should_roll_args):
        res = should_roll_args.pop()
        assert(intelligence.should_roll(*should_roll_args) == res)

    @pytest.mark.parametrize("participant_score, result", [(87, False), (94, True), (98, True)])
    def test_is_player_final_turn(self, intelligence, participant_score, result):
        assert (
            intelligence.is_player_final_turn(participant_score) == result
        )

    @pytest.mark.parametrize(
        "turn_total_score, bot_score, result", [(4, 70, False), (4, 90, True), (18, 80, True)]
    )
    def test_is_bot_final_turn(self, intelligence, turn_total_score, bot_score, result):
        assert (
            intelligence.is_bot_final_turn(
                turn_total_score,
                bot_score
            ) == result
        )

    @pytest.mark.parametrize("turn_total_points, result", [(12, False), (17, True), (23, True)])
    def test_is_optimal_turn_score(self, intelligence, turn_total_points, result):
        assert (
            intelligence.is_optimal_turn_score(turn_total_points) == result
        )

    @pytest.mark.parametrize("roll, result", [(1, False), (5, False), (8, True)])
    def test_is_max_turn_roll(self, intelligence, roll, result):
        assert intelligence.is_max_turn_roll(roll) == result

    @pytest.mark.parametrize(
        "points, result",
        [
            (85, False),
            (102, True),
            (100, True),
        ],
    )
    def test_is_winner_score(self, intelligence, points,result):
        assert intelligence.is_winner_score(points) is result

    @pytest.fixture(scope="function")
    def intelligence(self):
        return IntelligenceHigh(Game())
