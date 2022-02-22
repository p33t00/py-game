import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from IntelligenceLow import IntelligenceLow


class TestIntelligenceLow:
    @pytest.mark.parametrize("execution_number", range(5))
    def test_should_roll(self, intelligence, execution_number):
        decision = intelligence.should_roll()
        assert type(decision) == bool
        assert decision is True or decision is False

    @pytest.fixture(scope="function", autouse=True)
    def intelligence(self):
        return IntelligenceLow(None)
