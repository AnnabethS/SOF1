import unittest
import inspect

from seminarTesting import rod_cutting_2

class TestSeminarCode(unittest.TestCase):

    def testLength1(self):
        self.assertEqual(1, rod_cutting_2(1, [1, 5, 8, 9, 10, 17]))
        
    def testLength2(self):
        self.assertEqual(5, rod_cutting_2(2, [1, 5, 8, 9, 10, 17]))

    def testLength3(self):
        self.assertEqual(8, rod_cutting_2(3, [1, 5, 8, 9, 10, 17]))

    def testLength4(self):
        self.assertEqual(10, rod_cutting_2(4, [1, 5, 8, 9, 10, 17]))