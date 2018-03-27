import unittest

from MCState.MCSide.MCElementDirection import MCubeDirection
from unittest import TestCase

class MCElemetTest(TestCase):
    def test_direction_count(self):
        count = 0;
        for dir in MCubeDirection:
            count+=1
        assert count is 9

if __name__=="__main__":
    unittest.main()
