from MCState.MCSide.MCElementDirection import MCubeDirection


class MCSideState(object):
    """
    MCSideState is a model of Rubik's Cube side
    it is store values of each element(color of squares)
    """
    def __init__(self,side, string_value = None):
        if None == string_value:
            self.value = dict()
            for dir in MCubeDirection:
                self.value[dir]=side

    def __iter__(self):
        return iter( list(self.value.values())[1:] )

    def __str__(self):
        result = '>'+str(self.value[MCubeDirection.CENTER])+'|'
        for value in self:
            result+=(':'+str(value))
        return result

    def __getitem__(self, direction):
        return  self.value[direction]

    def __setitem__(self, direction, value):
        self.value[direction] = value

    # def __dict__(self):
    #     return self.value

    def line(self, direction):
        """
        get value of element in same line
        values are sorted by clock rotating direction
        :param direction: direction of element, which line want to get
        :return: list of element value, from the line
        """
        if direction is MCubeDirection.NORTH:
            return [
                self[MCubeDirection.NORTH_WEST], self[MCubeDirection.NORTH], self[MCubeDirection.NORTH_EAST]
            ]
        elif direction is MCubeDirection.EAST:
            return [
                self[MCubeDirection.NORTH_EAST], self[MCubeDirection.EAST], self[MCubeDirection.SOUTH_EAST]
            ]
        elif direction is MCubeDirection.SOUTH:
            return [
                self[MCubeDirection.SOUTH_EAST], self[MCubeDirection.SOUTH], self[MCubeDirection.SOUTH_WEST]
            ]
        elif direction is MCubeDirection.WEST:
            return [
                self[MCubeDirection.SOUTH_WEST], self[MCubeDirection.WEST], self[MCubeDirection.NORTH_WEST]
            ]
        else:
            raise ValueError("Incrrect Directon : " + direction)

    def set_line(self, direction, value):
        if direction is MCubeDirection.NORTH:
            self[MCubeDirection.NORTH_WEST] = value[0]
            self[MCubeDirection.NORTH]      = value[1]
            self[MCubeDirection.NORTH_EAST] = value[2]
        elif direction is MCubeDirection.EAST:
            self[MCubeDirection.NORTH_EAST] = value[0]
            self[MCubeDirection.EAST]       = value[1]
            self[MCubeDirection.SOUTH_EAST] = value[2]
        elif direction is MCubeDirection.SOUTH:
            self[MCubeDirection.SOUTH_EAST] = value[0]
            self[MCubeDirection.SOUTH]      = value[1]
            self[MCubeDirection.SOUTH_WEST] = value[2]
        elif direction is MCubeDirection.WEST:
            self[MCubeDirection.SOUTH_WEST] = value[0]
            self[MCubeDirection.WEST]       = value[1]
            self[MCubeDirection.NORTH_WEST] = value[2]
        else:
            raise ValueError("Incrrect Directon : " + direction)

    def rotate(self):
        """
        shift side value by clock rotating direction
        :return: None
        """
        temp_north = self.line(MCubeDirection.NORTH)
        temp_east = self.line(MCubeDirection.EAST)
        temp_south = self.line(MCubeDirection.SOUTH)
        temp_west = self.line(MCubeDirection.WEST)

        self.set_line(MCubeDirection.NORTH,temp_west)
        self.set_line(MCubeDirection.EAST,temp_north)
        self.set_line(MCubeDirection.SOUTH,temp_east)
        self.set_line(MCubeDirection.WEST,temp_south)

    def derotate(self):
        """
        shift side value by clock reverse rotating direction
        :return: None
        """
        temp_north = self.line(MCubeDirection.NORTH)
        temp_east = self.line(MCubeDirection.EAST)
        temp_south = self.line(MCubeDirection.SOUTH)
        temp_west = self.line(MCubeDirection.WEST)

        self.set_line(MCubeDirection.NORTH, temp_east)
        self.set_line(MCubeDirection.EAST, temp_south)
        self.set_line(MCubeDirection.SOUTH, temp_west)
        self.set_line(MCubeDirection.WEST, temp_north)

