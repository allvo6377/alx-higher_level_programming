#!/usr/bin/python3
"""This module creates a class that inherits from MyList"""


class MyList(list):
    """A custom list class that inherits from list and prints sorted."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        # Use super() to access the list methods
        sorted_list = super().copy()
        sorted_list.sort()
        print(sorted_list)
