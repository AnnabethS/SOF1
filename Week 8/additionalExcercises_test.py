import unittest
import inspect

from additionalExcercises import *

class test_print_all(unittest.TestCase):

    def testNormalInput(self):
        self.assertEqual("0\n1\n2\n3\n4\n", print_all([0,1,2,3,4]))

    def testEmptyInput(self):
        self.assertEqual("", print_all([]))

    def testNonIntInput(self):
        self.assertRaises(TypeError, print_all, (["bruh", "moment"]))
        self.assertRaises(TypeError, print_all, ("bruhmoment"))


class test_print_all_reverse(unittest.TestCase):

    def testNormalInput(self):
        self.assertEqual("4\n3\n2\n1\n0\n", print_all_reverse([0,1,2,3,4]))

    def testEmptyInput(self):
        self.assertEqual("", print_all_reverse([]))

    def testNonIntInput(self):
        self.assertRaises(TypeError, print_all_reverse, (["bruh", "moment"]))
        self.assertRaises(TypeError, print_all_reverse, ("bruhmoment"))


class test_to_binary(unittest.TestCase):

    def testNormalInput(self):
        self.assertEqual("1100101", to_binary(83))

