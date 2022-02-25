import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))


class TestPlayer:
    def test_dummy(self):
        assert False
