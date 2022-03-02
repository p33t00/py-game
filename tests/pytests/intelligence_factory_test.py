import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../../lib/intelligence/"))

from src.game import Game
from intelligence import Intelligence
from intelligence_factory import IntelligenceFactory
from intelligence_low import IntelligenceLow
from intelligence_high import IntelligenceHigh


class TestIntelligenceFactory:
    def test_get_game(self, factory):
        game = factory.get_game()
        assert(isinstance(game, Game))

    @pytest.mark.parametrize(
        "index, intelect",
        [
            (0, IntelligenceLow),
            (1, IntelligenceHigh),
        ],
    )
    def test_get_intelligence(self, factory, index, intelect):
        intelligence = factory.get_intelligence(index)
        assert(isinstance(intelligence, Intelligence))
        assert(isinstance(intelligence, intelect))

    @pytest.mark.xfail(raises=IndexError)
    def test_get_intelligence_invalid_input(self, factory):
        """Providing invalid user input that should trigger handled IndexError"""
        factory.get_intelligence(5)

    @pytest.mark.xfail(raises=TypeError)
    def test_get_intelligence_invalid_type(self, factory):
        """Initiate ValueError"""
        factory.get_intelligence("Invalid index")

    @pytest.fixture(scope="function")
    def factory(self):
        return IntelligenceFactory(Game())
