#!/usr/bin/python3
""" A class representing a square. """


class Square:
    """
    This class allows you to create and manipulate square objects.
    Each square is defined by its side length.
    """

    def __init__(self, size=0, position=(0, 0)):

        """Initialize a new Square.
            Args:
                size (int): The size of the new square.
                position (tuple): The position of the new square.
        """
        self.size = size
        self.position = position

    def area(self):
        square_area = self.__size * self.__size

