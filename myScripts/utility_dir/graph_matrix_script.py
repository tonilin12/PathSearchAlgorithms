from typing import Dict, Any

import numpy


class Edge:
    def __init__(self, weight=None, pi=None):
        self.weight = float(weight) if weight is not None else None
        self.pi = pi

    def to_string(self):
        print("weight: ",self.weight,"pi",self.pi)


class GraphMatrix:
    def __init__(self):
        self.edges: Dict[str, Dict[str, Any]] = {}

    def add_vertex(self, vertex):
        if vertex not in self.edges:
            self.edges[vertex] = {}

    def add_edge(self, start_vertex, end_vertex, weight=1):
        self.add_vertex(start_vertex)
        self.add_vertex(end_vertex)

        if end_vertex not in self.edges[start_vertex].keys():
            edge0=Edge(weight,start_vertex)
            self.edges[start_vertex][end_vertex] = edge0


    def display(self):
        for start_vertex, edges in self.edges.items():
            print("vertex:", start_vertex)
            for end_vertex, edge_ij in edges.items():
                if edge_ij.pi==start_vertex or edge_ij.pi is None:
                    print(start_vertex,"-",edge_ij.weight,"->", end_vertex)
                else:
                    pi =edge_ij.pi
                    edge_ik=self.edges[start_vertex][pi]
                    edge_kj=self.edges[pi][end_vertex]
                    print(start_vertex,"-",edge_ik.weight,"->", pi
                          ,"-",edge_kj.weight,"->",end_vertex
                          ," weight:", edge_ij.weight)


    def set_default(self):
        for vertex_i in self.edges.keys():
            for vertex_j in self.edges.keys():
                if vertex_i == vertex_j:
                    self.edges[vertex_i][vertex_j]=Edge(0,vertex_i)
                else:
                    if vertex_j not in self.edges[vertex_i].keys():
                        self.edges[vertex_i][vertex_j]=Edge(numpy.inf,None)


def read_to_graph_matrix_from_file(graph: GraphMatrix, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip().split(':')
                vertex = line[0].strip()
                str0 = ''.join(line[1:]).split('|')

                tuple_list = [tuple(pair.split(',')) for pair in str0]
                for neighbor, weight in tuple_list:
                    graph.add_edge(vertex, neighbor, int(weight))



    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    graph.set_default()
