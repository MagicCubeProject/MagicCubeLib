from unittest import TestCase

from MCState.MCState import MagicCubeState
from MCStep.MCMoves import MCubeMoves
from MCStep.MCStep import MCStep
from MCView.MCHtmlView import MCHtmlView


class TestMCStep(TestCase):
    def test_move(self):
        mc_state = MagicCubeState()
        print(mc_state)
        step = MCStep(mc_state)
        step.moves([MCubeMoves.UP_DOUBLE_DOWN_DOUBLE,MCubeMoves.FRONT_BACK_INVERS])
        print(mc_state)
        basicView = MCHtmlView(mc_state)
        basicView.render()
