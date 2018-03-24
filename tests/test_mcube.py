import unittest
from rcube.MagicCube import MCubeState
from rcube.MagicCubeFlags import MCubeSide

class MCubeStateTest(unittest.TestCase):
    def test_mcube_init(self):
        mc = MCubeState()
        print(mc)

if __name__=="__main__":
    mc = MCubeState()
    print(mc)
    nmc = mc.get_rotated_state(MCubeSide.FRONT)
