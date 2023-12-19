#!/usr/bin/python3
# 4-square.py

"""Defines a square"""


class Square:

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
