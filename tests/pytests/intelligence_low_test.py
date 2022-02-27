import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from src.game import Game
from src.intelligence import Intelligence
from src.intelligence_low import IntelligenceLow


class TestIntelligenceLow:
    def test_is_intelligence_cls(self):
        assert issubclass(IntelligenceLow, Intelligence)

    @pytest.mark.parametrize("execution_number", range(5))
    def test_should_roll(self, intelligence, execution_number):
        decision = intelligence.should_roll()
        assert type(decision) == bool
        assert decision is True or decision is False

    @pytest.mark.parametrize(
        "points, result",
        [
            (75, False),
            (105, True),
            (100, True),
        ],
    )
    def test_is_winner_score(self, intelligence, points, result):
        assert intelligence.is_winner_score(points) is result

    @pytest.fixture(scope="function")
    def intelligence(self):
        return IntelligenceLow(Game())
