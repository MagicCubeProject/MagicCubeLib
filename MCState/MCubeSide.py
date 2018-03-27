from enum import Enum, auto

from MCState.MCSide.MCElementDirection import MCubeDirection


class MCubeSide(Enum):
    FRONT   = auto()
    RIGHT   = auto()
    DOWN    = auto()
    UP      = auto()
    LEFT    = auto()
    BACK    = auto()

    def __str__(self):
        return str(self.name)

    def neighbor(self,direction):
        if self is MCubeSide.FRONT:
            if direction is MCubeDirection.NORTH:
                return MCubeSide.UP
            elif direction is MCubeDirection.EAST:
                return MCubeSide.RIGHT
            elif direction is MCubeDirection.SOUTH:
                return MCubeSide.DOWN
            elif direction is MCubeDirection.WEST:
                return MCubeSide.LEFT
            else:
                raise ValueError("Incrrect Directon : " + direction)
        elif self is MCubeSide.RIGHT:
            if direction is MCubeDirection.NORTH:
                return MCubeSide.UP
            elif direction is MCubeDirection.EAST:
                return MCubeSide.BACK
            elif direction is MCubeDirection.SOUTH:
                return MCubeSide.DOWN
            elif direction is MCubeDirection.WEST:
                return MCubeSide.FRONT
            else:
                raise ValueError("Incrrect Directon : " + direction)
        elif self is MCubeSide.BACK:
            if direction is MCubeDirection.NORTH:
                return MCubeSide.DOWN
            elif direction is MCubeDirection.EAST:
                return MCubeSide.RIGHT
            elif direction is MCubeDirection.SOUTH:
                return MCubeSide.UP
            elif direction is MCubeDirection.WEST:
                return MCubeSide.LEFT
            else:
                raise ValueError("Incrrect Directon : " + direction)
        elif self is MCubeSide.LEFT:
            if direction is MCubeDirection.NORTH:
                return MCubeSide.DOWN
            elif direction is MCubeDirection.EAST:
                return MCubeSide.BACK
            elif direction is MCubeDirection.SOUTH:
                return MCubeSide.UP
            elif direction is MCubeDirection.WEST:
                return MCubeSide.FRONT
            else:
                raise ValueError("Incrrect Directon : " + direction)
        elif self is MCubeSide.UP:
            if direction is MCubeDirection.NORTH:
                return MCubeSide.BACK
            elif direction is MCubeDirection.EAST:
                return MCubeSide.RIGHT
            elif direction is MCubeDirection.SOUTH:
                return MCubeSide.FRONT
            elif direction is MCubeDirection.WEST:
                return MCubeSide.LEFT
            else:
                raise ValueError("Incrrect Directon : " + direction)
        elif self is MCubeSide.DOWN:
            if direction is MCubeDirection.NORTH:
                return MCubeSide.FRONT
            elif direction is MCubeDirection.EAST:
                return MCubeSide.RIGHT
            elif direction is MCubeDirection.SOUTH:
                return MCubeSide.BACK
            elif direction is MCubeDirection.WEST:
                return MCubeSide.LEFT
            else:
                raise ValueError("Incrrect Directon : " + direction)
