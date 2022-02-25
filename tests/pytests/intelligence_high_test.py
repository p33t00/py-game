import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from constants import WINNER_SCORE
from src.intelligence import Intelligence
from src.intelligence_high import IntelligenceHigh


class TestIntelligenceHigh:
    def test_is_intelligence_cls(self):
        assert issubclass(IntelligenceHigh, Intelligence)

    """player_score, bot_score, turn_total_score, turn_roll_num"""

    @pytest.mark.parametrize(
        "should_roll_args",
        [
            (0, 0, 0, 0, True),  # beginning of the game
            (87, 91, 3, 3, True),  # bot last roll
            (98, 81, 3, 3, True),  # player last roll
            (87, 79, 17, 3, True),  # optimal turn score
            (87, 79, 10, 5, True),  # max turn roll score
            (37, 29, 26, 7, False),  # finish turn
            (77, 87, 18, 3, False),  # winning score
        ],
    )
    def test_should_roll(self, intelligence, should_roll_args):
        assert (
            intelligence.should_roll(
                should_roll_args[0],
                should_roll_args[1],
                should_roll_args[2],
                should_roll_args[3],
            ) == should_roll_args[4]
        )

    @pytest.mark.parametrize("participant_score", [(74, False), (94, True), (98, True)])
    def test_is_player_final_roll(self, intelligence, participant_score):
        assert (
            intelligence.is_player_final_roll(participant_score[0]) == participant_score[1]
        )

    """0 -> turn_total_score, 1 -> bot_score, 2 -> result"""

    @pytest.mark.parametrize(
        "participant_score", [(70, 4, False), (90, 4, True), (80, 18, True)]
    )
    def test_is_bot_final_roll(self, intelligence, participant_score):
        assert (
            intelligence.is_bot_final_roll(
                participant_score[0],
                participant_score[1]
            ) == participant_score[2]
        )

    @pytest.mark.parametrize("turn_total_points", [(12, False), (17, True), (23, True)])
    def test_is_optimal_turn_score(self, intelligence, turn_total_points):
        assert (
            intelligence.is_optimal_turn_score(turn_total_points[0]) == turn_total_points[1]
        )

    @pytest.mark.parametrize("roll_result", [(1, False), (5, False), (8, True)])
    def test_is_max_turn_roll(self, intelligence, roll_result):
        assert intelligence.is_max_turn_roll(roll_result[0]) == roll_result[1]

    @pytest.mark.parametrize(
        "points",
        [
            (85, False),
            (102, True),
            (100, True),
        ],
    )
    def test_is_winner_score(self, intelligence, points):
        assert intelligence.is_winner_score(points[0]) is points[1]

    @pytest.fixture(autouse=True, scope="function")
    def intelligence(self):
        return IntelligenceHigh(WINNER_SCORE)

    @pytest.fixture(params=[(74, False), (94, True), (98, True)])
    def participant_score(self, request):
        return request.param
