import builtins
from pathlib import Path
import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from lib.gui_helper import GUIHelper


class TestGUIHelper:
    def test_get_intro(self, gui):
        intro = gui.get_intro()
        assert(type(intro) is str)
        assert(len(intro) > 0)

    @pytest.mark.parametrize("answer, result", [("y", True), ("n", False)])
    def test_play_again(self, monkeypatch, gui, answer, result):
        monkeypatch.setattr(builtins, "input", lambda x: answer)
        assert(gui.play_again() == result)

    def test_get_picto_dice(self, gui, picto_dice):
        for i in range(1, 7):
            pd = gui.get_picto_dice(i)
            assert(type(pd) == str)
            assert(pd == picto_dice[i - 1])

    @pytest.mark.xfail(raises=IndexError)
    def test_get_picto_dice_fail(self, gui):
        gui.get_picto_dice(50)

    @pytest.fixture(scope="function")
    def gui(self):
        return GUIHelper()

    @pytest.fixture(scope="function")
    def picto_dice(self):
        return Path("assets/picto-dice.txt").read_text().split("\n\n")
