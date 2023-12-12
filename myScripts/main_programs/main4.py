from myScripts.utility_dir.Utility import *
from myScripts.graph_dir.graphfile import *
from myScripts.algorithm.PrimAlgorithm import *


def show_graph(list_raw, order):
    adjacency_list = create_adjacency_list(list_raw)
    draw_digraph(adjacency_list, order)


if __name__ == '__main__':
    file = "sorucefiles/adatok"

    dict0 = create_default_dict_from_file(file)
    prim_order_list = apply_prim(dict0)
    print(prim_order_list)
    print()
    print()
    show_graph(dict0, prim_order_list)
