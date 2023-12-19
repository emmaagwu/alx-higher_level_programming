#!/usr/bin/python3
# 5-square.py

"""Defines a square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initializies the square

        Args:
            size(int): The size of the square
        """
        self.__size = size

    @property
    def size(self):
        """gets the current value of size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the new value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
            return (self.__size)

    def area(self):
        """Returns the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
