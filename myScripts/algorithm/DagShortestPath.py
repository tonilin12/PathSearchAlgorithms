from typing import Optional, Any

from myScripts.algorithm.DepthFirstSearch import apply_dfs
from myScripts.utility_dir.CustomTypes import *


def apply_dag_path_search(graph_dict: Dict[Any, ColoredVertex],
                          start_point=None):
    result_list = []

    if start_point is None:
        start_point = list(graph_dict.keys())[0] if graph_dict else None
    else:

        if not (start_point in graph_dict):
            print("error: graph does not have Vertex ", start_point)
            print()
            return None

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
    for index, Vertex in graph_dict.items():
        Vertex.d = numpy.inf
        Vertex.pi = None

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

    return result_list
