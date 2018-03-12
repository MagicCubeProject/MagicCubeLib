import unittest
import logging

class BasicTest(unittest.TestCase):
    def test(self):
        logging.debug('Test Working')
        self.assertEqual(True,True)
