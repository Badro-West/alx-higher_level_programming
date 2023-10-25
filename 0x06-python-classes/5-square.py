#!/usr/bin/python3
""" A class representing a square. """


class Square:
    """
    This class allows you to create and manipulate square objects.
    Each square is defined by its side length.
    """

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    def area(self):
        square_area = self.__size * self.__size
        return (square_area)

    @property
    def size(self):
        """
        Retrieve the size (side length) of the square.

