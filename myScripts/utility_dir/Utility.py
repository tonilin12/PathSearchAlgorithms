from myScripts.graph_dir.graphfile import *
from myScripts.graph_dir.graphfile import draw_digraph
from myScripts.utility_dir.CustomTypes import *


def create_adjacency_list(elements):
    adjacency_list = {}

    for key, value in elements.items():
        current = value.neighbours
        adjacency_list[key] = []
        while current:
            adjacency_list[key].append((current.index, current.weight))
            current = current.next

    return adjacency_list


def show_adjacency_list(adjacency_list):
    for source, neighbors in adjacency_list.items():
        print(f"Source: {source}, Neighbors: {neighbors}")


def print_heads(graph_dict):
    for i, Vertex in graph_dict.items():
        print("source:", i)
        print("heads")
        current = Vertex.neighbours
        while current:
            print(f"Destination: {current.index}, Weight: {current.weight}")
            current = current.next


K = TypeVar('K')


def add_vertex_if_not_exists(graph_dict, vertex, colored_Vertexs=False):
    if vertex not in graph_dict:
        if colored_Vertexs:
            graph_dict[vertex] = ColoredVertex(vertex)
        else:
            graph_dict[vertex] = Vertex(vertex)


def add_elements(graph_dict, index, pair_list, colored_Vertexs=False):
    add_vertex_if_not_exists(graph_dict, index, colored_Vertexs)

    for elem in pair_list:
        e1, e2 = elem
        graph_dict[index].add_neighbour(e1, e2)
        add_vertex_if_not_exists(graph_dict, e1, colored_Vertexs)


def create_default_dict_from_file(filename, colored_Vertexs=False):
    graph = {}

    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            line = line.strip()
            if line:
                index = line.index('|')
                elem0 = line[:index]

                pair_list = [tuple(pair.split(','))
                             for pair in line.split('|')[1:]]

                add_elements(graph, elem0, pair_list, colored_Vertexs)

            line = file.readline()

    return graph


def show_graph(graph_dict, order):
    adjacency_list = create_adjacency_list(graph_dict)
    draw_digraph(adjacency_list, order)

