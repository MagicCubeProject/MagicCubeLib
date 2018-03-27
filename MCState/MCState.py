from MCState.MCSide.MCElementDirection import MCubeDirection
from MCState.MCSide.MCSideState import MCSideState
from MCState.MCubeSide import MCubeSide


class MagicCubeState(object):
    def __init__(self,string_value = None):
        if None == string_value:
            self.value = {}
            for side in MCubeSide:
                print("11")
                self.value[side] = MCSideState(side)

    def __getitem__(self, side):
        return self.value[side]

    def __setitem__(self, side, value):
        self.value[side] = value

    def __str__(self):
        result = str()
        for value in self:
            result+=+str(value)
        return result

    def get_neighbor_line(self,side,direction):
        work_side = self[side]
        neighbor = side.neighbor(direction)
        if neighbor.neighbor(MCubeDirection.NORTH) is side:
            return self[neighbor].line(MCubeDirection.NORTH)
        elif neighbor.neighbor(MCubeDirection.EAST) is side:
            return self[neighbor].line(MCubeDirection.EAST)
        elif neighbor.neighbor(MCubeDirection.SOUTH) is side:
            return self[neighbor].line(MCubeDirection.SOUTH)
        elif neighbor.neighbor(MCubeDirection.WEST) is side:
            return self[neighbor].line(MCubeDirection.WEST)

    def rotate(self,side):
        self.value[side].rotate()
        pass
