import builtins
from pathlib import Path
import sys
import os
import io
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from lib.gui_helper import GUIHelper


class TestGUIHelper:
    def test_get_intro(self, gui):
        intro = gui.get_intro()
        assert type(intro) is str
        assert len(intro) > 0

    @pytest.mark.parametrize("answer, result", [("y", True), ("n", False)])
    def test_play_again(self, monkeypatch, gui, answer, result):
        monkeypatch.setattr(builtins, "input", lambda x: answer)
        assert gui.play_again() == result

    @pytest.mark.parametrize("answer", [12, "hello", "yyyy"])
    def test_play_again_invalid_in(self, capsys, gui, answer):
        # monkeypatch.setattr(builtins, "input", lambda x: answer)
        sys.stdin = io.StringIO(f"{answer}\nn\n")
        gui.play_again()

        out, err = capsys.readouterr()

        assert(err == "")
        assert(out == "Play again ?\n (y/n):\nInvalid input. Please try again.\nPlay again ?\n (y/n):\n")

    def test_get_intelect_id(self, gui):
        sys.stdin = io.StringIO("1\n")
        idx = gui.get_intelect_id()
        assert(idx == 1)

    @pytest.mark.xfail()
    @pytest.mark.parametrize("uin", [-1, 5, "hello"])
    def test_get_intelect_id_fail(self, gui, uin):
        sys.stdin = io.StringIO(f"{uin}\n")
        gui.get_intelect_id()

    def test_get_picto_dice(self, gui, picto_dice):
        for i in range(1, 7):
            pd = gui.get_picto_dice(i)
            assert type(pd) == str
            assert pd == picto_dice[i - 1]

    @pytest.mark.xfail(raises=IndexError)
    def test_get_picto_dice_fail(self, gui):
        gui.get_picto_dice(50)

    def test_get_rules(self, gui):
        rules = Path("assets/rules_n_instruct.txt").read_text()
        assert(rules == gui.get_rules())

    @pytest.fixture(scope="function")
    def gui(self):
        return GUIHelper()

    @pytest.fixture(scope="function")
    def picto_dice(self):
        return Path("assets/picto-dice.txt").read_text().split("\n\n")
