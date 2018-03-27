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

    def test_rotate(self):
        mcs = MagicCubeState()
        state1 = str(mcs)
        print(state1)
        mcs.rotate(MCubeSide.FRONT)
        state2 = str(mcs)
        print(state2)
        self.assertNotEqual(state1,state2)
        mcs.rotate(MCubeSide.FRONT)
        mcs.rotate(MCubeSide.FRONT)
        mcs.rotate(MCubeSide.FRONT)
        state3 = str(mcs)
        print(state3)
        self.assertEqual(state1,state3)

    def test_derotate(self):
        mcs = MagicCubeState()
        state1 = str(mcs)
        print(state1)
        mcs.derotate(MCubeSide.FRONT)
        state2 = str(mcs)
        print(state2)
        self.assertNotEqual(state1,state2)
        mcs.derotate(MCubeSide.FRONT)
        mcs.derotate(MCubeSide.FRONT)
        mcs.derotate(MCubeSide.FRONT)
        state3 = str(mcs)
        print(state3)
        self.assertEqual(state1,state3)

    def test_rotate_and_derotate(self):
        mcs = MagicCubeState()
        state1 = str(mcs)
        print(state1)
        mcs.rotate(MCubeSide.FRONT)
        state2 = str(mcs)
        print(state2)
        self.assertNotEqual(state1,state2)
        mcs.derotate(MCubeSide.FRONT)
        state3 = str(mcs)
        print(state3)
        self.assertEqual(state1,state3)
