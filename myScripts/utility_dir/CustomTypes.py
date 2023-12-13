from typing import List, TypeVar, Dict

import numpy

K = TypeVar('K')


class Color:
    WHITE = "white"
    GRAY = "gray"
    BLACK = "black"


class NeighbourNode:

    def __init__(self, index=None, weight=None, next1=None):
        self.index = index
        self.weight = int(weight) if weight is not None else None
        self.next = next1


class Vertex:

    def __init__(self, index):

        self.neighbours = None
        self._neighbour_iterator = None
        self.d = numpy.inf
        self.pi = None
        self.index = index
        self.s = None
        self.e = None
        self.b = None

    def add_neighbour(self, destination, weight):
        new_node = NeighbourNode(destination, weight, None)

        if not self.neighbours:
            self.neighbours = new_node
            self._neighbour_iterator = self.neighbours
        else:
            self._neighbour_iterator.next = new_node
            self._neighbour_iterator = self._neighbour_iterator.next


class ColoredVertex(Vertex):
    def __init__(self, index):
        super().__init__(index)
        self.f = 0
        self.d = 0
        self.color = Color.WHITE




