from pip.utils import logging

from MCState.MCState import MagicCubeState
from MCState.MCubeSide import MCubeSide
from MCStep.MCMoves import MCubeMoves


class MCStep(object):
    def __init__(self , magicCubeState = None):
        if magicCubeState is None:
            self.magicCubeState = MagicCubeState()
        else:
            self.magicCubeState = magicCubeState

    def move(self,move_type = MCubeMoves.IDENTICAL):
        if move_type is MCubeMoves.IDENTICAL:
            pass

        elif move_type is MCubeMoves.FRONT:
            self.magicCubeState.rotate(MCubeSide.FRONT)
        elif move_type is MCubeMoves.RIGHT:
            self.magicCubeState.rotate(MCubeSide.RIGHT)
        elif move_type is MCubeMoves.DOWN:
            self.magicCubeState.rotate(MCubeSide.DOWN)
        elif move_type is MCubeMoves.UP:
            self.magicCubeState.rotate(MCubeSide.UP)
        elif move_type is MCubeMoves.LEFT:
            self.magicCubeState.rotate(MCubeSide.LEFT)
        elif move_type is MCubeMoves.BACK:
            self.magicCubeState.rotate(MCubeSide.BACK)

        elif move_type is MCubeMoves.FRONT_INVERS:
            self.magicCubeState.derotate(MCubeSide.FRONT)
        elif move_type is MCubeMoves.RIGHT_INVERS:
            self.magicCubeState.derotate(MCubeSide.RIGHT)
        elif move_type is MCubeMoves.DOWN_INVERS:
            self.magicCubeState.derotate(MCubeSide.DOWN)
        elif move_type is MCubeMoves.UP_INVERS:
            self.magicCubeState.derotate(MCubeSide.UP)
        elif move_type is MCubeMoves.LEFT_INVERS:
            self.magicCubeState.derotate(MCubeSide.LEFT)
        elif move_type is MCubeMoves.BACK_INVERS:
            self.magicCubeState.derotate(MCubeSide.BACK)

        elif move_type is MCubeMoves.FRONT_DOUBLE:
            self.magicCubeState.rotate(MCubeSide.FRONT)
            self.magicCubeState.rotate(MCubeSide.FRONT)
        elif move_type is MCubeMoves.RIGHT_DOUBLE:
            self.magicCubeState.rotate(MCubeSide.RIGHT)
            self.magicCubeState.rotate(MCubeSide.RIGHT)
        elif move_type is MCubeMoves.DOWN_DOUBLE:
            self.magicCubeState.rotate(MCubeSide.DOWN)
            self.magicCubeState.rotate(MCubeSide.DOWN)
        elif move_type is MCubeMoves.UP_DOUBLE:
            self.magicCubeState.rotate(MCubeSide.UP)
            self.magicCubeState.rotate(MCubeSide.UP)
        elif move_type is MCubeMoves.LEFT_DOUBLE:
            self.magicCubeState.rotate(MCubeSide.LEFT)
            self.magicCubeState.rotate(MCubeSide.LEFT)
        elif move_type is MCubeMoves.BACK_DOUBLE:
            self.magicCubeState.rotate(MCubeSide.BACK)
            self.magicCubeState.rotate(MCubeSide.BACK)

        elif move_type is MCubeMoves.FRONT_BACK:
            self.move(MCubeMoves.FRONT)
            self.move(MCubeMoves.BACK)
        elif move_type is MCubeMoves.FRONT_BACK_INVERS:
            self.move(MCubeMoves.FRONT)
            self.move(MCubeMoves.BACK_INVERS)
        elif move_type is MCubeMoves.FRONT_BACK_DOUBLE:
            self.move(MCubeMoves.FRONT)
            self.move(MCubeMoves.BACK_DOUBLE)
        elif move_type is MCubeMoves.RIGHT_LEFT:
            self.move(MCubeMoves.RIGHT)
            self.move(MCubeMoves.LEFT)
        elif move_type is MCubeMoves.RIGHT_LEFT_INVERS:
            self.move(MCubeMoves.RIGHT)
            self.move(MCubeMoves.LEFT_INVERS)
        elif move_type is MCubeMoves.RIGHT_LEFT_DOUBLE:
            self.move(MCubeMoves.RIGHT)
            self.move(MCubeMoves.LEFT_DOUBLE)
        elif move_type is MCubeMoves.UP_DOWN:
            self.move(MCubeMoves.UP)
            self.move(MCubeMoves.DOWN)
        elif move_type is MCubeMoves.UP_DOWN_INVERS:
            self.move(MCubeMoves.UP)
            self.move(MCubeMoves.DOWN_INVERS)
        elif move_type is MCubeMoves.UP_DOWN_DOUBLE:
            self.move(MCubeMoves.UP)
            self.move(MCubeMoves.DOWN_DOUBLE)

        elif move_type is MCubeMoves.FRONT_INVERS_BACK:
            self.move(MCubeMoves.FRONT_INVERS)
            self.move(MCubeMoves.BACK)
        elif move_type is MCubeMoves.FRONT_INVERS_BACK_INVERS:
            self.move(MCubeMoves.FRONT_INVERS)
            self.move(MCubeMoves.BACK_INVERS)
        elif move_type is MCubeMoves.FRONT_INVERS_BACK_DOUBLE:
            self.move(MCubeMoves.FRONT_INVERS)
            self.move(MCubeMoves.BACK_DOUBLE)
        elif move_type is MCubeMoves.RIGHT_INVERS_LEFT:
            self.move(MCubeMoves.RIGHT_INVERS)
            self.move(MCubeMoves.LEFT)
        elif move_type is MCubeMoves.RIGHT_INVERS_LEFT_INVERS:
            self.move(MCubeMoves.RIGHT_INVERS)
            self.move(MCubeMoves.LEFT_INVERS)
        elif move_type is MCubeMoves.RIGHT_INVERS_LEFT_DOUBLE:
            self.move(MCubeMoves.RIGHT_INVERS)
            self.move(MCubeMoves.LEFT_DOUBLE)
        elif move_type is MCubeMoves.UP_INVERS_DOWN:
            self.move(MCubeMoves.UP_INVERS)
            self.move(MCubeMoves.DOWN)
        elif move_type is MCubeMoves.UP_INVERS_DOWN_INVERS:
            self.move(MCubeMoves.UP_INVERS)
            self.move(MCubeMoves.DOWN_INVERS)
        elif move_type is MCubeMoves.UP_INVERS_DOWN_DOUBLE:
            self.move(MCubeMoves.UP)
            self.move(MCubeMoves.DOWN_DOUBLE)

        elif move_type is MCubeMoves.FRONT_DOUBLE_BACK:
            self.move(MCubeMoves.FRONT_DOUBLE)
            self.move(MCubeMoves.BACK)
        elif move_type is MCubeMoves.FRONT_DOUBLE_BACK_INVERS:
            self.move(MCubeMoves.FRONT_DOUBLE)
            self.move(MCubeMoves.BACK_INVERS)
        elif move_type is MCubeMoves.FRONT_DOUBLE_BACK_DOUBLE:
            self.move(MCubeMoves.FRONT_DOUBLE)
            self.move(MCubeMoves.BACK_DOUBLE)
        elif move_type is MCubeMoves.RIGHT_DOUBLE_LEFT:
            self.move(MCubeMoves.RIGHT_DOUBLE)
            self.move(MCubeMoves.LEFT)
        elif move_type is MCubeMoves.RIGHT_DOUBLE_LEFT_INVERS:
            self.move(MCubeMoves.RIGHT_DOUBLE)
            self.move(MCubeMoves.LEFT_INVERS)
        elif move_type is MCubeMoves.RIGHT_DOUBLE_LEFT_DOUBLE:
            self.move(MCubeMoves.RIGHT_DOUBLE)
            self.move(MCubeMoves.LEFT_DOUBLE)
        elif move_type is MCubeMoves.UP_DOUBLE_DOWN:
            self.move(MCubeMoves.UP_DOUBLE)
            self.move(MCubeMoves.DOWN)
        elif move_type is MCubeMoves.UP_DOUBLE_DOWN_INVERS:
            self.move(MCubeMoves.UP_DOUBLE)
            self.move(MCubeMoves.DOWN_INVERS)
        elif move_type is MCubeMoves.UP_DOUBLE_DOWN_DOUBLE:
            self.move(MCubeMoves.UP_DOUBLE)
            self.move(MCubeMoves.DOWN_DOUBLE)

    def moves(self,move_types):
        for move_type in move_types:
            self.move(move_type)
