from matplotlib.pyplot import show
import networkx as nx
from myScripts.graph_dir.Visualize_Algorithm import *
from myScripts.utility_dir.Utility import *


def do_drawing(graph, adjacency_list, order):
    for source, edges in adjacency_list.items():
        for edge in edges:
            destination, weight = edge
            graph.add_edge(source, destination, weight=weight)

    animate_graph(graph, order)


def draw_digraph(adjacency_list, order):
    graph = nx.DiGraph()
    do_drawing(graph, adjacency_list, order)


def draw_graph(adjacency_list, order):
    graph = nx.Graph()
    do_drawing(graph, adjacency_list, order)
