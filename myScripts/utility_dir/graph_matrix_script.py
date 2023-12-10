from typing import Dict, Any


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
            self.edges[start_vertex][end_vertex] = weight

    def display(self):
        for start_vertex, edges in self.edges.items():
            print("vertex:",start_vertex)
            for end_vertex, weight in edges.items():
                print(f"Edge from {start_vertex} to {end_vertex} "
                      f"with weight {weight}")


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
