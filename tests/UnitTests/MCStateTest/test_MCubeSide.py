from unittest import TestCase

from MCState.MCSide.MCElementDirection import MCubeDirection
from MCState.MCubeSide import MCubeSide


class TestMCubeSide(TestCase):
    def test_neighbor(self):
        for side in MCubeSide:
            print(side.neighbor(MCubeDirection.NORTH))
