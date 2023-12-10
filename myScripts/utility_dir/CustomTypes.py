from typing import List, TypeVar, Dict

import numpy

K = TypeVar('K')


class Color:
    WHITE = "white"
    GRAY = "gray"
    BLACK = "black"


class NeighbourElem:
    def __init__(self, index=None):
        self.index = index
        self.weight = 0


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


class Graph:
    def __init__(self):
        self.vertices = {}
        self.adj_matrix = []

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            index = len(self.vertices)
            self.vertices[vertex] = index
            # Initialize a new row and column in the adjacency matrix
            for row in self.adj_matrix:
                row.append(0)
            self.adj_matrix.append([0] * index)
            for i in range(index):
                self.adj_matrix[i].append(0)

    def add_edge(self, start_vertex, end_vertex, weight=1):
        if start_vertex in self.vertices and end_vertex in self.vertices:
            start_index = self.vertices[start_vertex]
            end_index = self.vertices[end_vertex]
            self.adj_matrix[start_index][end_index] = weight

    def display_adjacency_matrix(self):
        for row in self.adj_matrix:
            print(row)


