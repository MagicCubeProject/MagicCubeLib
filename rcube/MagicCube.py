from rcube.MagicCubeFlags import MCubeMoves
from rcube.MagicCubeFlags import MCubeSide
from rcube.MagicCubeFlags import MCubeDirection

class MCubeState(object):
    def __init__(self,string_value = None):
        if string_value is None:
            self.solve_count = 0
            self.value = {
                MCubeSide.FRONT : MCubeSideState(MCubeSide.FRONT),
                MCubeSide.RIGHT : MCubeSideState(MCubeSide.RIGHT),
                MCubeSide.DOWN  : MCubeSideState(MCubeSide.DOWN),
                MCubeSide.UP    : MCubeSideState(MCubeSide.UP),
                MCubeSide.LEFT  : MCubeSideState(MCubeSide.LEFT),
                MCubeSide.BACK  : MCubeSideState(MCubeSide.BACK),
            }

    def __str__(self):
        result = str()
        result += str(self.value[MCubeSide.FRONT])
        result += str(self.value[MCubeSide.RIGHT])
        result += str(self.value[MCubeSide.DOWN])
        result += str(self.value[MCubeSide.UP])
        result += str(self.value[MCubeSide.LEFT])
        result += str(self.value[MCubeSide.BACK])
        return result

    def __get_side(self, side):
        return self.value[side]

    def __set_side(self, side, value):
        self.value[side] = value

    def __get_copy(self):
        new_cube_state = MCubeState()
        new_cube_state.__set_side(
            MCubeSide.FRONT,
            self.__get_side(MCubeSide.FRONT)
        )
        new_cube_state.__set_side(
            MCubeSide.RIGHT,
            self.__get_side(MCubeSide.RIGHT)
        )
        new_cube_state.__set_side(
            MCubeSide.DOWN,
            self.__get_side(MCubeSide.DOWN)
        )
        new_cube_state.__set_side(
            MCubeSide.UP,
            self.__get_side(MCubeSide.UP)
        )
        new_cube_state.__set_side(
            MCubeSide.LEFT,
            self.__get_side(MCubeSide.LEFT)
        )
        new_cube_state.__set_side(
            MCubeSide.BACK,
            self.__get_side(MCubeSide.BACK)
        )
        return new_cube_state

    def __get_neighbor_line(self,side,direction):
        work_side = self.__get_side(side)
        side_neighbors = work_side.get_neighbors()
        neighbor_side = self.__get_side(side_neighbors[direction])
        neighbor_direction = neighbor_side.get_neighbor_direction(
            side
        )
        line = neighbor_side.get_line(neighbor_direction)
        return line

    def __set_neighbor_line(self,side,direction,line):
        work_side = self.__get_side(side)
        side_neighbors = work_side.get_neighbors()
        neighbor_side = self.__get_side(side_neighbors[direction])
        neighbor_direction = neighbor_side.get_neighbor_direction(
            side
        )
        neighbor_side.set_line(neighbor_direction,line)

    def get_rotated_state(self, side):
        print(20*'\'')
        print("side :",side)
        print(self.__get_neighbor_line(
            side,
            MCubeDirection.NORTH
        ))
        self.__set_neighbor_line(
            side,
            MCubeDirection.NORTH,
            [MCubeSide.LEFT,MCubeSide.UP,MCubeSide.DOWN]
        )

        print(self.__get_neighbor_line(
            side,
            MCubeDirection.NORTH
        ))


class MCubeSideState(object):
    def __init__(self, side):
        self.side = side
        self.neighbors = self.get_neighbors()
        self.value = {
            MCubeDirection.NORTH_WEST   : side,
            MCubeDirection.NORTH        : side,
            MCubeDirection.NORTH_EAST   : side,
            MCubeDirection.WEST         : side,
            MCubeDirection.CENTER       : side,
            MCubeDirection.EAST         : side,
            MCubeDirection.SOUTH_WEST   : side,
            MCubeDirection.SOUTH        : side,
            MCubeDirection.SOUTH_EAST   : side,
        }

    def __str__(self):
        result = str()
        result += ( ':'+str(self.value[MCubeDirection.NORTH_WEST]) )
        result += ( ':'+str(self.value[MCubeDirection.NORTH]) )
        result += ( ':'+str(self.value[MCubeDirection.NORTH_EAST]) )
        result += ( ':'+str(self.value[MCubeDirection.WEST]) )
        result += ( ':'+str(self.value[MCubeDirection.CENTER]) )
        result += ( ':'+str(self.value[MCubeDirection.EAST]) )
        result += ( ':'+str(self.value[MCubeDirection.SOUTH_WEST]) )
        result += ( ':'+str(self.value[MCubeDirection.SOUTH]) )
        result += ( ':'+str(self.value[MCubeDirection.SOUTH_EAST]) )
        return result

    def get_value(self,direction):
        return self.value[direction]

    def set_value(self,direction,value):
        self.value[direction]=value

    def get_line(self,direction):
        if direction is MCubeDirection.NORTH:
            return [
                self.value[MCubeDirection.NORTH_WEST],
                self.value[MCubeDirection.NORTH],
                self.value[MCubeDirection.NORTH_EAST],
            ]
        elif direction is MCubeDirection.EAST:
            return [
                self.value[MCubeDirection.NORTH_EAST],
                self.value[MCubeDirection.EAST],
                self.value[MCubeDirection.SOUTH_EAST],
            ]
        elif direction is MCubeDirection.SOUTH:
            return [
                self.value[MCubeDirection.SOUTH_EAST],
                self.value[MCubeDirection.SOUTH],
                self.value[MCubeDirection.SOUTH_WEST],
            ]
        elif direction is MCubeDirection.WEST:
            return [
                self.value[MCubeDirection.SOUTH_WEST],
                self.value[MCubeDirection.WEST],
                self.value[MCubeDirection.NORTH_WEST],
            ]

    def set_line(self, direction, value):
        if direction is MCubeDirection.NORTH:
            self.value[MCubeDirection.NORTH_WEST]   = value[0]
            self.value[MCubeDirection.NORTH]        = value[1]
            self.value[MCubeDirection.NORTH_EAST]   = value[2]
        elif direction is MCubeDirection.EAST:
            self.value[MCubeDirection.NORTH_EAST]   = value[0]
            self.value[MCubeDirection.EAST]         = value[1]
            self.value[MCubeDirection.SOUTH_EAST]   = value[2]
        elif direction is MCubeDirection.SOUTH:
            self.value[MCubeDirection.SOUTH_EAST]   = value[0]
            self.value[MCubeDirection.SOUTH]        = value[1]
            self.value[MCubeDirection.SOUTH_WEST]   = value[2]
        elif direction is MCubeDirection.WEST:
            self.value[MCubeDirection.SOUTH_WEST]   = value[0]
            self.value[MCubeDirection.WEST]         = value[1]
            self.value[MCubeDirection.NORTH_WEST]   = value[2]


    def get_neighbors(self):
        if self.side is MCubeSide.FRONT:
            return {
                MCubeDirection.NORTH    : MCubeSide.UP,
                MCubeDirection.WEST     : MCubeSide.LEFT,
                MCubeDirection.EAST     : MCubeSide.RIGHT,
                MCubeDirection.SOUTH    : MCubeSide.DOWN,
            }
        elif self.side is MCubeSide.RIGHT:
            return {
                MCubeDirection.NORTH    : MCubeSide.UP,
                MCubeDirection.EAST     : MCubeSide.BACK,
                MCubeDirection.SOUTH    : MCubeSide.DOWN,
                MCubeDirection.WEST     : MCubeSide.FRONT,
            }
        elif self.side is MCubeSide.DOWN:
            return {
                MCubeDirection.NORTH    : MCubeSide.FRONT,
                MCubeDirection.WEST     : MCubeSide.LEFT,
                MCubeDirection.EAST     : MCubeSide.RIGHT,
                MCubeDirection.SOUTH    : MCubeSide.BACK,
            }
        elif self.side is MCubeSide.UP:
            return {
                MCubeDirection.NORTH    : MCubeSide.BACK,
                MCubeDirection.WEST     : MCubeSide.LEFT,
                MCubeDirection.EAST     : MCubeSide.RIGHT,
                MCubeDirection.SOUTH    : MCubeSide.FRONT,
            }
        elif self.side is MCubeSide.LEFT:
            return {
                MCubeDirection.NORTH    : MCubeSide.DOWN,
                MCubeDirection.WEST     : MCubeSide.FRONT,
                MCubeDirection.EAST     : MCubeSide.BACK,
                MCubeDirection.SOUTH    : MCubeSide.UP,
            }
        elif self.side is MCubeSide.BACK:
            return {
                MCubeDirection.NORTH    : MCubeSide.DOWN,
                MCubeDirection.WEST     : MCubeSide.LEFT,
                MCubeDirection.EAST     : MCubeSide.RIGHT,
                MCubeDirection.SOUTH    : MCubeSide.UP,
            }

    def get_neighbor_direction(self,neighbor_side):
        neighbors = self.get_neighbors()
        for neighbor_direction in neighbors.keys():
            if neighbor_side is neighbors[neighbor_direction]:
                return neighbor_direction

    def get_rotated_state(self):
            side_value = self.get_value(MCubeDirection.CENTER)
            new_state = MCubeSideState(side_value)
            new_state.set_value(
                MCubeDirection.NORTH_WEST,
                self.get_value(MCubeDirection.SOUTH_WEST)
            )
            new_state.set_value(
                MCubeDirection.NORTH_EAST,
                self.get_value(MCubeDirection.NORTH_WEST)
            )
            new_state.set_value(
                MCubeDirection.SOUTH_EAST,
                self.get_value(MCubeDirection.NORTH_EAST)
            )
            new_state.set_value(
                MCubeDirection.SOUTH_WEST,
                self.get_value(MCubeDirection.SOUTH_EAST)
            )
            new_state.set_value(
                MCubeDirection.NORTH,
                self.get_value(MCubeDirection.WEST)
            )
            new_state.set_value(
                MCubeDirection.EAST,
                self.get_value(MCubeDirection.NORTH)
            )
            new_state.set_value(
                MCubeDirection.SOUTH,
                self.get_value(MCubeDirection.EAST)
            )
            new_state.set_value(
                MCubeDirection.WEST,
                self.get_value(MCubeDirection.SOUTH)
            )
            return new_state

    def get_derotated_state(self):
            side_value = self.get_value(MCubeDirection.CENTER)
            new_state = MCubeSideState(side_value)
            new_state.set_value(
                MCubeDirection.NORTH_WEST,
                self.get_value(MCubeDirection.NORTH_EAST)
            )
            new_state.set_value(
                MCubeDirection.NORTH_EAST,
                self.get_value(MCubeDirection.SOUTH_EAST)
            )
            new_state.set_value(
                MCubeDirection.SOUTH_EAST,
                self.get_value(MCubeDirection.SOUTH_WEST)
            )
            new_state.set_value(
                MCubeDirection.SOUTH_WEST,
                self.get_value(MCubeDirection.NORTH_WEST)
            )
            new_state.set_value(
                MCubeDirection.NORTH,
                self.get_value(MCubeDirection.EAST)
            )
            new_state.set_value(
                MCubeDirection.EAST,
                self.get_value(MCubeDirection.SOUTH)
            )
            new_state.set_value(
                MCubeDirection.SOUTH,
                self.get_value(MCubeDirection.WEST)
            )
            new_state.set_value(
                MCubeDirection.WEST,
                self.get_value(MCubeDirection.NORTH)
            )
            return new_state
