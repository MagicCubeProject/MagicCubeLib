from unittest import TestCase

from MCState.MCSide.MCElementDirection import MCubeDirection
from MCState.MCState import MagicCubeState
from MCState.MCubeSide import MCubeSide


class TestMCubeSide(TestCase):
    def test_neighbor(self):
        for side in MCubeSide:
            print(side.neighbor(MCubeDirection.NORTH))

    def test_numeric(self):
        mc_state = MagicCubeState()
        print( mc_state.numeric() )
        self.assertEquals(
            "111111111222222222333333333444444444555555555666666666",
            mc_state.numeric()
        )
        print( len(mc_state.numeric()))
        self.assertEquals(
            54,
            len(mc_state.numeric())
        )

    def test_json(selfs):
        mc_state = MagicCubeState()
        print( mc_state.json() )
