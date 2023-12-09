import os
from typing import TypeVar

from myScripts.utility_dir.CustomTypes import *
from myScripts.graph_dir.graphfile import *


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
    for i, edge in graph_dict.items():
        print("source:", i)
        print("heads")
        current = edge.neighbours
        while current:
            print(f"Destination: {current.index}, Weight: {current.weight}")
            current = current.next



K = TypeVar('K')


def add_vertex_if_not_exists(graph_dict, vertex, colored_edges=False):
    if vertex not in graph_dict:
        if colored_edges:
            graph_dict[vertex] = ColoredEdge(vertex)
        else:
            graph_dict[vertex] = Edge(vertex)


def add_elements(graph_dict, index, pair_list, colored_edges=False):
    add_vertex_if_not_exists(graph_dict, index, colored_edges)

    for elem in pair_list:
        e1, e2 = elem
        graph_dict[index].add_neighbour(e1, e2)
        add_vertex_if_not_exists(graph_dict, e1, colored_edges)


def create_default_dict_from_file(filename, colored_edges=False):
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

                add_elements(graph, elem0, pair_list, colored_edges)

            line = file.readline()

    return graph

def show_graph(graph_dict, order):
    adjacency_list = create_adjacency_list(graph_dict)
    draw_digraph(adjacency_list, order)


def process_and_show_dfs_graph(file, apply_algorithm, get_topology=False):
    graph_dict = create_default_dict_from_file(file, colored_edges=True)

    bfs_order = apply_algorithm(graph_dict, get_topology)

    show_graph(graph_dict, bfs_order)


