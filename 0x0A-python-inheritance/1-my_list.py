#!/usr/bin/python3
"""
my list module
"""


class MyList(list):
    """subclass of list"""

    def print_sorted(self):
        """returns a sorted list"""
        print(sorted(self))
