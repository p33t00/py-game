import builtins
import sys
import os
import pytest
# from unittest import mock

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from UI import UI
from constants import WINNER_SCORE
from IntelligenceLow import IntelligenceLow
from IntelligenceHigh import IntelligenceHigh


class TestUI:
    @pytest.mark.parametrize('id_to_intellect', [
        (0, IntelligenceLow),
        (1, IntelligenceHigh),
    ])
    def test_get_intelligence(self, ui, id_to_intellect):
        intelligence = ui.get_intelligence(id_to_intellect[0], WINNER_SCORE)
        assert type(intelligence) == id_to_intellect[1]

    def test_get_intelligence_invalid_input(self, ui, monkeypatch):
        '''Providing invalid user input "5" that should cause handled IndexError'''
        monkeypatch.setattr(builtins, 'input', lambda x: '1')
        intelligence = ui.get_intelligence(5, WINNER_SCORE)
        assert type(intelligence) == IntelligenceLow

    def test_get_intelligence_fail(self):
        '''maybe make more tests for this method'''
        assert(False)
        
    def test_load_picto_dice(self, ui):
        ui.load_picto_dice()
        pd = ui.get_picto_dice(1)
        assert(type(pd) == str)
        assert(len(pd) > 0)

    @pytest.fixture(autouse=True, scope="function")
    def ui(self):
        return UI()
