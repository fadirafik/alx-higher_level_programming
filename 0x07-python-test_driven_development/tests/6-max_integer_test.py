#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class testint(unittest.TestCase):

    def test_max_integer(self):
        result = max_integer([1,2,3,4,3])
        self.assertEqual(result, 4)