from enum import Enum

class MCubeMoves(Enum):
    FRONT   = 1
    RIGHT   = 2
    DOWN    = 3
    UP      = 4
    LEFT    = 5
    BACK    = 6

    FRONT_INVERS    = 7
    RIGHT_INVERS    = 8
    DOWN_INVERS     = 9
    UP_INVERS       = 10
    LEFT_INVERS     = 11
    BACK_INVERS     = 12

    FRONT_DOUBLE    = 13
    RIGHT_DOUBLE    = 14
    DOWN_DOUBLE     = 15
    UP_DOUBLE       = 16
    LEFT_DOUBLE     = 17
    BACK_DOUBLE     = 18

    FRONT_BACK          = 19
    FRONT_BACK_INVERS   = 20
    FRONT_BACK_DOUBLE   = 21
    RIGHT_LEFT          = 22
    RIGHT_LEFT_INVERS   = 23
    RIGHT_LEFT_DOUBLE   = 24
    UP_DOWN             = 25
    UP_DOWN_INVERS      = 26
    UP_DOWN_DOUBLE      = 27

    FRONT_INVERS_BACK           = 28
    FRONT_INVERS_BACK_INVERS    = 29
    FRONT_INVERS_BACK_DOUBLE    = 30
    RIGHT_INVERS_LEFT           = 31
    RIGHT_INVERS_LEFT_INVERS    = 32
    RIGHT_INVERS_LEFT_DOUBLE    = 33
    UP_INVERS_DOWN              = 34
    UP_INVERS_DOWN_INVERS       = 35
    UP_INVERS_DOWN_DOUBLE       = 36

    FRONT_DOUBLE_BACK           = 37
    FRONT_DOUBLE_BACK_INVERS    = 38
    FRONT_DOUBLE_BACK_DOUBLE    = 40
    RIGHT_DOUBLE_LEFT           = 41
    RIGHT_DOUBLE_LEFT_INVERS    = 42
    RIGHT_DOUBLE_LEFT_DOUBLE    = 43
    UP_DOUBLE_DOWN              = 44
    UP_DOUBLE_DOWN_INVERS       = 45
    UP_DOUBLE_DOWN_DOUBLE       = 46


class MCubeState(object):
    def __init__(self, list_code = range(6*9)):
        self.list_code = list_code

    def __str__(self):
        result = str()
        for code in self.list_code:
            if len(str(code))>1:
                result+=':{}'.format(str(code))
            else:
                result+=':0{}'.format(str(code))
        return result

if __name__=="__main__":
    for move in MCubeMoves:
        print (move)
    mc = MCubeState()
    print(mc,len(str(mc)))
