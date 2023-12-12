from myScripts.algorithm.QueueBermanFord import apply_berman_ford
from myScripts.graph_dir.graphfile import *
from myScripts.utility_dir.Utility import create_default_dict_from_file


def show_graph(list_raw, order):
    adjacency_list = create_adjacency_list(list_raw)
    draw_digraph(adjacency_list, order)


if __name__ == '__main__':
    file = "sorucefiles/adatok"

    graph_raw = create_default_dict_from_file(file)
    berman_ford_path = apply_berman_ford(graph_raw)
    show_graph(graph_raw,berman_ford_path)


