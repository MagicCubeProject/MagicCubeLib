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
    def __init__(self,state_set=None):
        self.dir_dict = dict()
        if not state_set is None:
            self.dir_dict[MCubeDirection.NORTH_WEST] = state_set[0]
            self.dir_dict[MCubeDirection.NORTH] = state_set[1]
            self.dir_dict[MCubeDirection.NORTH_EAST] = state_set[2]
            self.dir_dict[MCubeDirection.WEST] = state_set[3]
            self.dir_dict[MCubeDirection.CENTER] = state_set[4]
            self.dir_dict[MCubeDirection.EAST] = state_set[5]
            self.dir_dict[MCubeDirection.SOUTH_WEST] = state_set[6]
            self.dir_dict[MCubeDirection.SOUTH] = state_set[7]
            self.dir_dict[MCubeDirection.SOUTH_EAST] = state_set[8]

    def set_dir(self,dir,value):
        self.dir_dict[dir] = value


    def __str__(self):
        string_type = str()
        string_type+= (':'+str(self.dir_dict[MCubeDirection.NORTH_WEST]))
        string_type+= (':'+str(self.dir_dict[MCubeDirection.NORTH]))
        string_type+= (':'+str(self.dir_dict[MCubeDirection.NORTH_EAST]))
        string_type+= (':'+str(self.dir_dict[MCubeDirection.WEST]))
        string_type+= (':'+str(self.dir_dict[MCubeDirection.CENTER]))
        string_type+= (':'+str(self.dir_dict[MCubeDirection.EAST]))
        string_type+= (':'+str(self.dir_dict[MCubeDirection.SOUTH_WEST]))
        string_type+= (':'+str(self.dir_dict[MCubeDirection.SOUTH]))
        string_type+= (':'+str(self.dir_dict[MCubeDirection.SOUTH_EAST]))
        return string_type

    def get_list(self):
        list_type = list()
        list_type.append(self.dir_dict[MCubeDirection.NORTH_WEST])
        list_type.append(self.dir_dict[MCubeDirection.NORTH])
        list_type.append(self.dir_dict[MCubeDirection.NORTH_EAST])
        list_type.append(self.dir_dict[MCubeDirection.WEST])
        list_type.append(self.dir_dict[MCubeDirection.CENTER])
        list_type.append(self.dir_dict[MCubeDirection.EAST])
        list_type.append(self.dir_dict[MCubeDirection.SOUTH_WEST])
        list_type.append(self.dir_dict[MCubeDirection.SOUTH])
        list_type.append(self.dir_dict[MCubeDirection.SOUTH_EAST])
        return list_type

    def rotated_to(self):
        temp_state = MCubeSideState()
        temp_state.set_dir(
            MCubeDirection.CENTER,
            self.dir_dict[MCubeDirection.CENTER]
        )
        temp_state.set_dir(
            MCubeDirection.SOUTH_WEST,
            self.dir_dict[MCubeDirection.NORTH_WEST]
        )
        temp_state.set_dir(
            MCubeDirection.NORTH_WEST,
            self.dir_dict[MCubeDirection.NORTH_EAST]
        )
        temp_state.set_dir(
            MCubeDirection.NORTH_EAST,
            self.dir_dict[MCubeDirection.SOUTH_EAST]
        )
        temp_state.set_dir(
            MCubeDirection.SOUTH_EAST,
            self.dir_dict[MCubeDirection.SOUTH_WEST]
        )
        temp_state.set_dir(
            MCubeDirection.WEST,
            self.dir_dict[MCubeDirection.NORTH]
        )
        temp_state.set_dir(
            MCubeDirection.NORTH,
            self.dir_dict[MCubeDirection.EAST]
        )
        temp_state.set_dir(
            MCubeDirection.EAST,
            self.dir_dict[MCubeDirection.SOUTH]
        )
        temp_state.set_dir(
            MCubeDirection.SOUTH,
            self.dir_dict[MCubeDirection.WEST]
        )
        return MCubeSideState


if __name__ == "__main__":
    for move in MCubeMoves:
        print(move)
    print(20*'_')
    for side in MCubeSide:
        print(side)

    print(20*'_')
    for dir in MCubeDirection:
        print(dir)
    print(20*'_')
    m = MCubeState()
    print(m)
    print(m.get_list())
    a =  m.get_state(MCubeMoves.IDENTICAL)
    print(a)
