#!/usr/bin/python3

"""singly linked list implemented here"""


class Node:
    """Node class init bruv"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Singly list class"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        string = ''
        node = self.__head
        while node:
            string = f'{string}{node.data}'
            if node.next_node:
                string = f'{string}\n'
            node = node.next_node
        return string

    def sorted_insert(self, value):
        if not self.__head:
            self.__head = Node(value)
        elif self.__head.data >= value:
            tmp = self.__head
            self.__head = Node(value)
            self.__head.next_node = tmp
        else:
            node = self.__head
            while node.next_node and value > node.next_node.data:
                node = node.next_node
            tmp = node.next_node
            node.next_node = Node(value)
            node.next_node.next_node = tmp
