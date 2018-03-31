from _operator import neg
from enum import Flag, auto, Enum


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

    # def __not__(self):
    #     if self is MCubeMoves.IDENTICAL:
    #         return MCubeMoves.IDENTICAL
    #     elif self is MCubeMoves.IDENTICAL:
    #         return MCubeMoves.IDENTICAL
    #
    #
    # def __add__(self, other):
    #     if self is MCubeMoves.IDENTICAL:
    #         return other
    #     if other is MCubeMoves.FRONT:
    #         return MCubeMoves.FRONT_INVERS
    #


# class MCubeMoves(Enum):
#     IDENTICAL = 0
#
#     FRONT   = 1
#     RIGHT   = 2
#     DOWN    = 3
#     UP      = 4
#     LEFT    = 5
#     BACK    = 6
#
#     FRONT_INVERS    = -1
#     RIGHT_INVERS    = -2
#     DOWN_INVERS     = -3
#     UP_INVERS       = -4
#     LEFT_INVERS     = -5
#     BACK_INVERS     = -6
#
#     def __neg__(self):
#         for move in MCubeMoves:
#             if self.value+move.value==0:
#                 return move
#         return None
#
#     def __add__(self, other):
#         if self is -other:
#             return MCubeMoves.IDENTICAL
#         else:
#             return None
#
#     def __sub__(self, other):
#         if self is other:
#             return MCubeMoves.IDENTICAL
#         else:
#             return None
#
#     def __and__(self, other):
#         if (self.value+other.value)%7 is 0:
#             return True
#         else:
#             False
