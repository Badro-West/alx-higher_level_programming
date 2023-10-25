#!/usr/bin/python3
""" class Node that defines a node of a singly linked list """


class Node:
    """ class Node that defines a node of a singly linked list """

    def __init__(self, data=0, next_node=None):

        """Initialize a new Node.
            Args:
                data (int): The data of the node of a singly linked list.
                next_node (Node): The next_node of the node of a ssl.
        """
        self.data = data
        self.next_node = None

    @property
    def data(self):
        """
        Retrieve the data of the node of a singly linked list.

        Returns:
            int: The data of the node of a singly linked list.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Set the the data part of the node of a singly linked list.

        Args:
            value (int): The data part of the node of a singly linked list.

        Raises:
            TypeError: data must be an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next_node of a singly linked list.

        Returns:
            Node: The next node of a singly linked list.
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Set the the next_node of a singly linked list.

        Args:
            value (Node): The next_node of a singly linked list.

        Raises:
            TypeError: next_node must be a Node object.
        """
        if not isinstance(value, Node) and value is not None:

