import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from constants import WINNER_SCORE
from Intelligence import Intelligence
from IntelligenceLow import IntelligenceLow


class TestIntelligenceLow:
    def test_is_intelligence_cls(self):
        assert issubclass(IntelligenceLow, Intelligence)

    @pytest.mark.parametrize("execution_number", range(5))
    def test_should_roll(self, intelligence, execution_number):
        decision = intelligence.should_roll()
        assert type(decision) == bool
        assert decision is True or decision is False

    @pytest.mark.parametrize('points', [
        (75, False),
        (105, True),
        (100, True),
    ])
    def test_is_winner_score(self, intelligence, points):
        assert (intelligence.is_winner_score(points[0]) is points[1])

    @pytest.fixture(scope="function", autouse=True)
    def intelligence(self):
        return IntelligenceLow(WINNER_SCORE)
