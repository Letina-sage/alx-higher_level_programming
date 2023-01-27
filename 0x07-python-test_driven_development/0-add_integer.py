#!/usr/bin/python3
"""
module contains function that adds
two integers a and b and returns the sum
"""


def add_integer(a, b=98):
    """
        adds 2 given  integers and returns the sum.
        If a float is passed it should be typecasted to an int
    """

    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
