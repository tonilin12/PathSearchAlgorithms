from typing import Dict, Optional, TypeVar

from myScripts.utility_dir.CustomTypes import *

import heapq
import numpy

K = TypeVar('K')


def apply_dijkstra(graph_dict: Dict[K, Edge], start_point: K = None):
    result_list = []

    if start_point is None:
        start_point = list(graph_dict.keys())[0] if graph_dict else None
    else:

        if not (start_point in graph_dict):
            print("error: graph does not have edge ", start_point)
            print()
            return None

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
    return result_list


def find_cheapest_path(graph_dict: Dict[K, Edge],
                       start_point0: K = None,
                       destination0: K = None):
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
    print()
    print("utvonal")
    print(path)
    print()
    return path
