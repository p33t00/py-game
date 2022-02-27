import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from src.game import Game


class TestGame:
    def test_get_winner_score(self, game):
        win_score = game.get_winner_score()
        assert type(win_score) is int
        assert win_score == 100

    @pytest.mark.parametrize(
        "participant_score",
        [
            (50, False),
            (100, True),
            (120, True),
        ],
    )
    def test_has_won(self, game, participant_score):
        assert game.has_won(participant_score[0]) == participant_score[1]

    @pytest.mark.xfail(raises=TypeError, strict=True)
    @pytest.mark.parametrize(
        "participant_score",
        [
            "helllo",
            False,
            True,
        ],
    )
    def test_has_won_fail(self, game, participant_score):
        assert game.has_won(participant_score[0]) == participant_score[1]

    @pytest.fixture(scope="function")
    def game(self):
        return Game()
