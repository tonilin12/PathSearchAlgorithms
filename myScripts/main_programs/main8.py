from myScripts.algorithm.DagShortestPath import apply_dag_path_search
from myScripts.utility_dir.Utility import *
from myScripts.graph_dir.graphfile import draw_digraph
from myScripts.algorithm.BreathFirstSearch import *


def show_graph(list_raw, order):
    adjacency_list = create_adjacency_list(list_raw)
    draw_digraph(adjacency_list, order)


if __name__ == '__main__':
    file = "sourcefiles/adatok"

    graph_raw = create_default_dict_from_file(file, colored_Vertexs=True)
    dag_path = apply_dag_path_search(graph_raw)
    print("dag_path:", dag_path)
    show_graph(graph_raw, dag_path)
