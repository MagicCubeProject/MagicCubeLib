from unittest import TestCase

from MCState.MCState import MagicCubeState
from MCState.MCubeSide import MCubeSide
from MCView.MCHtmlView import MCHtmlView


class TestMCHtmlView(TestCase):
    def test_render(self):
        basicView = MCHtmlView()
        path = basicView.render(save_to_file=False)
        print(path)

    def test_rotate(self):
        mc_state = MagicCubeState()
        basicView = MCHtmlView(mc_state)
        path = basicView.render()
        print(path)
