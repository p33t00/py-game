import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from lib.guiHelper import GUIHelper


class TestGUIHelper:
    def test_get_intro(self):
        assert False
