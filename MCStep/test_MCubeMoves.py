import operator
from unittest import TestCase

from MCStep.MCMoves import MCubeMoves


class TestMCubeMoves(TestCase):
    def test_add(self):
        for move in MCubeMoves:
            print(move, -move)
            print(move-move)

    def test_and(self):
        print(10*"*")
        for move in MCubeMoves:
            for other_move in MCubeMoves:
                if move & other_move:
                    print(move, other_move)
