import sys
import os
import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../.."))

from Participant import Participant


class TestParticipant:
    @pytest.mark.parametrize('points', [4, 2, 6])
    def test_add_get_total_points(self, participant, points):
        '''Testing add() & get_total_points() methods'''
        assert(participant.get_total_points() == 0)
        participant.add_points(points)
        assert(participant.get_total_points() == points)
        participant.add_points(points)
        assert(participant.get_total_points() == points * 2)

    def test_reset_total_points(self, participant):
        assert(participant.get_total_points() == 0)

        participant.add_points(35)
        participant.reset_total_points()
        assert(participant.get_total_points() == 0)

        participant.add_points(51)
        participant.reset_total_points()
        assert(participant.get_total_points() == 0)

    def test_set_name(self, participant):
        '''Testing get_name() & set_name() methods'''
        assert(participant.get_name() == 'default')
        participant.set_name('John')
        assert(participant.get_name() == 'John')
        participant.set_name('Lilly')
        assert(participant.get_name() == 'Lilly')

    @pytest.fixture(autouse=True)
    def participant(self):
        return Participant()
