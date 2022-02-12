import unittest
import sys

sys.path.insert(0, '/home/p33t/Study/py-game')

from Intelligence import Intelligence

class Intelligence_test(unittest.TestCase):
    def test_get_logic_simple(self):
        roll_again = Intelligence().get_logic_simple(21, 5, 3)
        # dummy arguments passed
        self.assertIs(roll_again, False if not roll_again else True)
        
        # check if ever returns True
        # chekc if ever returns False
        
    def test_get_logic_difficult(self):
        pass