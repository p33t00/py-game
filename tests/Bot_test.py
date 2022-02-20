import sys, os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from Bot import Bot
from IntelligenceLow import IntelligenceLow

class TestBot():
    def test_roll_again(self, bot):
        decision = bot.roll_again(0,0,0,0)
        assert type(decision) == bool
        assert decision is True or decision is False


    @pytest.fixture(autouse=True, scope='function')
    def bot(self):
        return Bot('Computer', IntelligenceLow())