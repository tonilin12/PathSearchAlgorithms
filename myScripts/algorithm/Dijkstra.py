import heapq
from typing import Optional, Any

import numpy
from myScripts.utility_dir.CustomTypes import *
from myScripts.utility_dir.Utility import get_start_point


def apply_dijkstra(graph_dict: Dict[Any, Vertex], start_point=None):
    result_list = []

    start_point = get_start_point(graph_dict,start_point)


    start_point_elem = graph_dict[start_point]
    start_point_elem.d = 0

    min_queue = []

    for elem_u in graph_dict.values():
        if elem_u != start_point_elem:
            heapq.heappush(min_queue, (numpy.inf, elem_u.index))

    elem_u = start_point_elem
    while elem_u.d < numpy.inf and min_queue:
        node: Optional[NeighbourNode]
        node = elem_u.neighbours
        while node:
            elem_v = graph_dict[node.index]
            if elem_v.d > elem_u.d + node.weight:
                min_queue.remove((elem_v.d, elem_v.index))
                elem_v.pi = elem_u.index
                elem_v.d = elem_u.d + node.weight
                heapq.heappush(min_queue, (elem_v.d, elem_v.index))

            node = node.next
        priority, u = heapq.heappop(min_queue)

        elem_u = graph_dict[u]
        vertex = (elem_u.pi, elem_u.index)
        print(elem_u.pi, "->", elem_u.index, "d: ", elem_u.d)
        result_list.append(vertex)

    print(result_list)
    print()

    return result_list


def find_cheapest_path(graph_dict: Dict[Any, Vertex],
                       start_point0=None,
                       destination0=None):
    if not (start_point0 in graph_dict) or not (destination0 in graph_dict):
        return None
    apply_dijkstra(graph_dict, start_point0)

    path = []

    elem_v = graph_dict[destination0]
    while elem_v.pi is not None:
        vertex = (elem_v.pi, elem_v.index)
        path.append(vertex)
        elem_v = graph_dict[elem_v.pi]

    path = path[::-1]
    print("utvonal:",path)
    print()
    return path
