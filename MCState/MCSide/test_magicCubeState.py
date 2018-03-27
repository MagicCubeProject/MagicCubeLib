from unittest import TestCase

from MCState.MCSide.MCElementDirection import MCubeDirection
from MCState.MCState import MagicCubeState
from MCState.MCubeSide import MCubeSide


class TestMagicCubeState(TestCase):
    def test_MCubeSide(self):
        for side in MCubeSide:
            print(side)
            neighbor = side.neighbor(MCubeDirection.NORTH)
            print("neighbor : ",neighbor)

    def test_init(self):
        mcs = MagicCubeState()
        del mcs


    def test_get_neighbor_line(self):
        mcs = MagicCubeState()
        for side in MCubeSide:
            print(mcs[side])

    # def test_get_neighbor_line(self):
    #     mcs = MagicCubeState()
    #     mcs.get_neighbor_line(MCubeSide.FRONT,MCubeDirection.NORTH)
    #     self.assertEquals()
