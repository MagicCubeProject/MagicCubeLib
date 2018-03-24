from enum import Flag,auto

# todo , add flag
class MCubeMoves(Flag):
    IDENTICAL = auto()

    FRONT   = auto()
    RIGHT   = auto()
    DOWN    = auto()
    UP      = auto()
    LEFT    = auto()
    BACK    = auto()

    FRONT_INVERS    = auto()
    RIGHT_INVERS    = auto()
    DOWN_INVERS     = auto()
    UP_INVERS       = auto()
    LEFT_INVERS     = auto()
    BACK_INVERS     = auto()

    FRONT_DOUBLE    = auto()
    RIGHT_DOUBLE    = auto()
    DOWN_DOUBLE     = auto()
    UP_DOUBLE       = auto()
    LEFT_DOUBLE     = auto()
    BACK_DOUBLE     = auto()

    FRONT_BACK          = FRONT | BACK
    FRONT_BACK_INVERS   = FRONT | BACK_INVERS
    FRONT_BACK_DOUBLE   = FRONT | BACK_DOUBLE
    RIGHT_LEFT          = RIGHT | LEFT
    RIGHT_LEFT_INVERS   = RIGHT | LEFT_INVERS
    RIGHT_LEFT_DOUBLE   = RIGHT | LEFT_DOUBLE
    UP_DOWN             = UP | DOWN
    UP_DOWN_INVERS      = UP | DOWN_INVERS
    UP_DOWN_DOUBLE      = UP | DOWN_DOUBLE

    FRONT_INVERS_BACK           = FRONT_INVERS | BACK
    FRONT_INVERS_BACK_INVERS    = FRONT_INVERS | BACK_INVERS
    FRONT_INVERS_BACK_DOUBLE    = FRONT_INVERS | BACK_DOUBLE
    RIGHT_INVERS_LEFT           = RIGHT_INVERS | LEFT
    RIGHT_INVERS_LEFT_INVERS    = RIGHT_INVERS | LEFT_INVERS
    RIGHT_INVERS_LEFT_DOUBLE    = RIGHT_INVERS | LEFT_DOUBLE
    UP_INVERS_DOWN              = UP_INVERS | DOWN
    UP_INVERS_DOWN_INVERS       = UP_INVERS | DOWN_INVERS
    UP_INVERS_DOWN_DOUBLE       = UP_INVERS | DOWN_DOUBLE

    FRONT_DOUBLE_BACK           = FRONT_DOUBLE | BACK
    FRONT_DOUBLE_BACK_INVERS    = FRONT_DOUBLE | BACK_INVERS
    FRONT_DOUBLE_BACK_DOUBLE    = FRONT_DOUBLE | BACK_DOUBLE
    RIGHT_DOUBLE_LEFT           = RIGHT_DOUBLE | LEFT
    RIGHT_DOUBLE_LEFT_INVERS    = RIGHT_DOUBLE | LEFT_INVERS
    RIGHT_DOUBLE_LEFT_DOUBLE    = RIGHT_DOUBLE | LEFT_DOUBLE
    UP_DOUBLE_DOWN              = UP_DOUBLE | DOWN
    UP_DOUBLE_DOWN_INVERS       = UP_DOUBLE | DOWN_INVERS
    UP_DOUBLE_DOWN_DOUBLE       = UP_DOUBLE | DOWN_DOUBLE

class MCubeSide(Flag):
    FRONT   = auto()
    RIGHT   = auto()
    DOWN    = auto()
    UP      = auto()
    LEFT    = auto()
    BACK    = auto()

    def __str__(self):
        return str(self.value)


class MCubeDirection(Flag):
    CENTER  = auto()
    NORTH   = auto()
    EAST    = auto()
    SOUTH   = auto()
    WEST    = auto()
    NORTH_WEST = NORTH | WEST
    NORTH_EAST = NORTH | EAST
    SOUTH_WEST = SOUTH | WEST
    SOUTH_EAST = SOUTH | EAST
