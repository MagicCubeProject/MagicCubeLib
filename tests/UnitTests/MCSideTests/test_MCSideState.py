from unittest import TestCase

from MCState.MCSide.MCElementDirection import MCubeDirection
from MCState.MCSide.MCSideState import MCSideState


class TestMCSideState(TestCase):
    def test_initialization(self):
        front_side = MCSideState(1)
        for dir in MCubeDirection:
            value = front_side[dir]
            self.assertEquals(1,1)

    def test_state_to_str(self):
        front_side = MCSideState("TEST.SIDE")
        print(front_side)
        self.assertEquals(
            ">TEST.SIDE|:TEST.SIDE:TEST.SIDE:TEST.SIDE:TEST.SIDE:TEST.SIDE:TEST.SIDE:TEST.SIDE:TEST.SIDE",
            str(front_side)
        )

    def test_side_iter(self):
        front_side = MCSideState("TEST.SIDE")
        element_couunt = 0
        for element in front_side:
            element_couunt +=1
        self.assertEquals(element_couunt,8)

    def test_set(self):
        front_side = MCSideState(1)
        for dir in MCubeDirection:
            value = front_side[dir]
            self.assertEquals(1,1)
        for dir in MCubeDirection:
            front_side[dir] = 2
        for dir in MCubeDirection:
            value = front_side[dir]
            self.assertEquals(2,2)

    def test_rotate(self):
        front_side = MCSideState(1)
        front_side[MCubeDirection.NORTH] = "TestValue"
        front_side.rotate()
        self.assertEquals(front_side[MCubeDirection.NORTH],1)
        self.assertEquals(front_side[MCubeDirection.EAST],"TestValue")
        front_side.derotate()
        self.assertEquals(front_side[MCubeDirection.NORTH],"TestValue")
        self.assertEquals(front_side[MCubeDirection.EAST],1)

    # def test_dict_parse(self):
    #     front_side = MCSideState(1)
    #     print(dict(front_side))
    #
