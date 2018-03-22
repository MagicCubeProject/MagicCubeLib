from MagicCubeFlags import MCubeMoves
from MagicCubeFlags import MCubeSide
from MagicCubeFlags import MCubeDirection

class MCubeState(object):
    def __init__(self,state_set=range(6*9)):
        side_len = int(len(state_set)/6)
        self.sides_dict = dict()
        self.sides_dict[MCubeSide.FRONT] = MCubeSideState(state_set[0:side_len])
        self.sides_dict[MCubeSide.RIGHT] = MCubeSideState(state_set[side_len:2*side_len])
        self.sides_dict[MCubeSide.DOWN] = MCubeSideState(state_set[2*side_len:3*side_len])
        self.sides_dict[MCubeSide.UP] = MCubeSideState(state_set[3*side_len:4*side_len])
        self.sides_dict[MCubeSide.LEFT] = MCubeSideState(state_set[4*side_len:5*side_len])
        self.sides_dict[MCubeSide.BACK] = MCubeSideState(state_set[5*side_len:6*side_len])

    def __str__(self):
        string_type = str()
        for side in MCubeSide:
            string_type += str(self.sides_dict[side])
        return string_type

    def get_list(self):
        list_type = list()
        for side in MCubeSide:
            list_type+= self.sides_dict[side].get_list()
        return list_type


    def get_state(self, move = MCubeMoves.IDENTICAL):
        if move is MCubeMoves.IDENTICAL:
            return MCubeState(self.get_list())
        elif move is MCubeMoves.FRONT:
            return None

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
        elif direction is MCubeDirection.WAST:
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
        elif direction is MCubeDirection.WAST:
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

        def get_rotated_state():
            side_value = self.get_value(MCubeDirection.CENTER)
            newState = MCubeSideState(side_value)
            newState.set_value(
                MCubeDirection.NORTH_WEST,
                self.get_value(MCubeDirection.SOUTH_WEST)
            )
            newState.set_value(
                MCubeDirection.NORTH_EAST,
                self.get_value(MCubeDirection.NORTH_WEST)
            )
            newState.set_value(
                MCubeDirection.SOUTH_EAST,
                self.get_value(MCubeDirection.NORTH_EAST)
            )
            newState.set_value(
                MCubeDirection.SOUTH_WEST,
                self.get_value(MCubeDirection.SOUTH_EAST)
            )
            newState.set_value(
                MCubeDirection.NORTH,
                self.get_value(MCubeDirection.WEST)
            )
            newState.set_value(
                MCubeDirection.EAST,
                self.get_value(MCubeDirection.NORTH)
            )
            newState.set_value(
                MCubeDirection.SOUTH,
                self.get_value(MCubeDirection.EAST)
            )
            newState.set_value(
                MCubeDirection.WEST,
                self.get_value(MCubeDirection.SOUTH)
            )
            return newState
