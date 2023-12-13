from typing import Optional, Any

from myScripts.algorithm.DepthFirstSearch import apply_dfs
from myScripts.utility_dir.Utility import *


def apply_dag_path_search(graph_dict: Dict[Any, ColoredVertex],
                          start_point=None):
    result_list = []

    start_point = get_start_point(graph_dict,start_point)
    start_point_elem = graph_dict[start_point]
    start_point_elem.d = 0
    back_Vertex = []

    dfs_path, topology_order = apply_dfs(graph_dict, back_Vertex)
    topology_stack = topology_order[::-1]
    if len(back_Vertex) == 0:
        result_list = create_dag_path(graph_dict, topology_stack)

    return result_list


def create_dag_path(graph_dict: Dict[K, ColoredVertex],
                    topology_stack: List[K]):
    result_list = []
    for index, vertex in graph_dict.items():
        vertex.d = numpy.inf
        vertex.pi = None

    s = topology_stack.pop()
    elem_u = graph_dict[s]
    elem_u.d = 0
    while topology_stack:
        node: Optional[NeighbourNode]
        node = elem_u.neighbours
        while node:
            elem_v = graph_dict[node.index]
            if elem_v.d > elem_u.d + node.weight:
                elem_v.pi = elem_u.index
                elem_v.d = elem_u.d + node.weight
            node = node.next

        u = topology_stack.pop()
        elem_u = graph_dict[u]

        vertex = (elem_u.pi, elem_u.index)
        print(elem_u.pi, "->", elem_u.index, "d: ", elem_u.d)
        result_list.append(vertex)
        print()

    return result_list



