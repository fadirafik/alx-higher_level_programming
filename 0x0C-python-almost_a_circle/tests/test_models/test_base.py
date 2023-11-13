#!/usr/bin/python3
"""base unittests"""


import os
import unittest
from models.base import Base


class testBase_init(unittest.TestCase):
    """unitesst for testing initiation"""

    def test_narguments(self):
        ba = Base()
        bb = Base()
        self.assertEqual(ba.id, bb.id -1)


if __name__ == "__main__":
    unittest.main()