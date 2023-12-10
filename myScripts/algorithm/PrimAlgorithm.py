import heapq
from typing import Optional, Any

import numpy
from myScripts.utility_dir.CustomTypes import *


def apply_prim(graph_dict: Dict[Any, Vertex]):
    result_list = []
    start_point = list(graph_dict.keys())[0] if graph_dict else None

    start_point_elem = graph_dict[start_point]
    start_point_elem.d = 0

    min_queue = []
    heapq.heappush(min_queue, (start_point_elem.d, start_point_elem.index))

    for elem_u in graph_dict.values():
        if elem_u != start_point_elem:
            heapq.heappush(min_queue, (numpy.inf, elem_u.index))

    while min_queue:
        priority, u = heapq.heappop(min_queue)
        elem_u = graph_dict[u]

        print()
        print("out| value:", u, "|pi:", elem_u.pi, "|priority:", priority)

        vertex = (elem_u.pi, u)
        if elem_u.pi != None:
            result_list.append(vertex)

        neighbours_node: Optional[NeighbourNode]
        neighbours_node = elem_u.neighbours
        while neighbours_node:
            v = neighbours_node.index
            elem_v = graph_dict[v]

            target_value = v
            is_in_queue = any(value == target_value for _, value in min_queue)

            weight_uv = neighbours_node.weight

            if is_in_queue and elem_v.d > float(weight_uv):
                min_queue.remove((elem_v.d, elem_v.index))
                elem_v.d = float(weight_uv)
                elem_v.pi = u
                heapq.heappush(min_queue, (elem_v.d, elem_v.index))
                print("in: priority:", elem_v.d, " value", elem_v.index)

            neighbours_node = neighbours_node.next

    print()
    return result_list
