from myScripts.utility_dir.Utility import *
from myScripts.graph_dir.graphfile import *
from myScripts.algorithm.KruskalAlgorithm import *


def show_graph(list_raw, order):
    adjacency_list = create_adjacency_list(list_raw)
    draw_digraph(adjacency_list, order)


if __name__ == '__main__':
    file = "sorucefiles/adatok"

    graph_raw = create_default_dict_from_file(file)
    kruskal_order = apply_kruskal(graph_raw)
    show_graph(graph_raw, kruskal_order)
