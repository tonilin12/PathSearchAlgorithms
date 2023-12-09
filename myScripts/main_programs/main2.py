from myScripts.algorithm.DepthFirstSearch import apply_dfs
from myScripts.utility_dir.Utility import *
from myScripts.graph_dir.graphfile import draw_digraph


def show_graph(list_raw, order):
    adjacency_list = create_adjacency_list(list_raw)
    draw_digraph(adjacency_list, order)


if __name__ == '__main__':
    file = "adatok"

    graph_raw = create_default_dict_from_file(file,colored_edges=True)
    dfs_list,topology_list = apply_dfs(graph_raw)

    topology_path=[]
    for i in range(len(topology_list)-1):
        vertex=(topology_list[i],topology_list[i+1])
        topology_path.append(vertex)
    show_graph(graph_raw,dfs_list)
