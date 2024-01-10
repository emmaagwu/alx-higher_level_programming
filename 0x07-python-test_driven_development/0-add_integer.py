#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a (int or float) The first number
        b (int or float) The second number. Defaults to 98

    Raises:
        TypeError: if a or b is not an integer or a float

    Return:
       The sum of a and b
    """

    """ Checks if a is an integer or a float """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return(a + b)
