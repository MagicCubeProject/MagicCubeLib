import unittest
from gtpy.groupoid import Groupoid

class GroupoidTest(unittest.TestCase):
    def test_simple_set(self):
        mySet = set(range(1, 4))

        def operation(e1, e2):
            return (e1*e2%3)+1
        g1 = Groupoid(mySet, operation)
        self.assertIsNotNone(g1, None)

    def test_neg_simple_set(self):
        mySet = set([1,2,4])

        def operation(e1, e2):
            return (e1*e2%3)+1

        try:
            g1 = Groupoid(mySet, operation)
        except Exception as e:
            print("a")

    def test_empty_function_simple_set(self):
        mySet = set([1,2,4])
        operation = None
        g1 = Groupoid(mySet, operation)
        self.assertIsNotNone(g1, None)
