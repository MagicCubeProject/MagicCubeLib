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

    def __iter__(self):
        return iter( list(self.value.values()))

    def __getitem__(self, side):
        return self.value[side]

    def __setitem__(self, side, value):
        self.value[side] = value

    def __str__(self):
        result = str()
        for value in self:
            result+=str(value)
        return result

    def __get_neighbor_line(self,side,direction):
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

    def __set_neighbor_line(self,side,direction ,value):
        work_side = self[side]
        neighbor = side.neighbor(direction)
        if neighbor.neighbor(MCubeDirection.NORTH) is side:
            self[neighbor].set_line(MCubeDirection.NORTH, value)
        elif neighbor.neighbor(MCubeDirection.EAST) is side:
            self[neighbor].set_line(MCubeDirection.EAST, value)
        elif neighbor.neighbor(MCubeDirection.SOUTH) is side:
            self[neighbor].set_line(MCubeDirection.SOUTH, value)
        elif neighbor.neighbor(MCubeDirection.WEST) is side:
            self[neighbor].set_line(MCubeDirection.WEST,value)

    def rotate(self,side):
        self.value[side].rotate()
        temp_north_line = self.__get_neighbor_line(side,MCubeDirection.NORTH)
        temp_east_line = self.__get_neighbor_line(side,MCubeDirection.EAST)
        temp_south_line = self.__get_neighbor_line(side,MCubeDirection.SOUTH)
        temp_west_line = self.__get_neighbor_line(side,MCubeDirection.WEST)
        self.__set_neighbor_line(side,MCubeDirection.NORTH,temp_west_line)
        self.__set_neighbor_line(side,MCubeDirection.EAST,temp_north_line)
        self.__set_neighbor_line(side,MCubeDirection.SOUTH,temp_east_line)
        self.__set_neighbor_line(side,MCubeDirection.WEST,temp_south_line)

    def derotate(self,side):
        self.value[side].derotate()
        temp_north_line = self.__get_neighbor_line(side,MCubeDirection.NORTH)
        temp_east_line = self.__get_neighbor_line(side,MCubeDirection.EAST)
        temp_south_line = self.__get_neighbor_line(side,MCubeDirection.SOUTH)
        temp_west_line = self.__get_neighbor_line(side,MCubeDirection.WEST)
        self.__set_neighbor_line(side,MCubeDirection.NORTH,temp_east_line)
        self.__set_neighbor_line(side,MCubeDirection.EAST,temp_south_line)
        self.__set_neighbor_line(side,MCubeDirection.SOUTH,temp_west_line)
        self.__set_neighbor_line(side,MCubeDirection.WEST,temp_north_line)
