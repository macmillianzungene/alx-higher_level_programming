#!/usr/bin/python3
"""
This module defines a Node class and a SinglyLinkedList class
"""


class Node:
    """
    A class that defines a node of a singly linked list by:
    - Private instance attribute: data
    - Private instance attribute: next_node
    - Instantiation with data and next_node: def __init__(self, data, next_node=None)
    """

    def __init__(self, data, next_node=None):
        """
        Initialize the Node instance

        Parameters:
        - data (int): data of the node
        - next_node (Node): next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data of the Node instance
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the Node instance

        Parameters:
        - value (int): data of the node
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next_node of the Node instance
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next_node of the Node instance

        Parameters:
        - value (Node): next node in the list
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list by:
    - Private instance attribute: head
    - Simple instantiation: def __init__(self)
    - Public instance method: def sorted_insert(self, value)
    """

    def __init__(self):
        """
        Initialize the SinglyLinkedList instance
        """
        self.__head = None

    def __str__(self):
        """
        Print the entire list in stdout, one node number by line
        """
        values = []
        node = self.__head
        while node is not None:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list (increasing order)

        Parameters:
        - value (int): data of the new node
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node

