from typing import Dict, Optional, TypeVar, Tuple

from myScripts.utility_dir.CustomTypes import *

import heapq

K = TypeVar('K')


def apply_kruskal(edge_dict: Dict[K, Edge]):
    vertex_set = []

    for edge in edge_dict.values():
        make_set(edge)

    k = len(edge_dict)
    min_queue = []

    for edge in edge_dict.values():
        node: Optional[NeighbourNode]
        node = edge.neighbours
        while node:
            vertex = (edge.index, node.index)
            heapq.heappush(min_queue, (node.weight, vertex))

            node = node.next

    while k > 1 and min_queue:
        weight, vertex = heapq.heappop(min_queue)
        print("out: ", weight, "|", vertex)


        u_k, v_k = vertex

        x = findSet(edge_dict, u_k)
        y = findSet(edge_dict, v_k)

        if x != y:
            union(edge_dict, x, y)
            vertex_set.append(vertex)


            k =k- 1



    print(vertex_set)
    print()
    print()
    return vertex_set


def make_set(edge: Optional[Edge]):
    edge.s = 1
    edge.pi = edge.index


def findSet(graph: Dict[K, Edge], v):
    elem_v: Optional[Edge]
    elem_v = graph[v]

    if elem_v.pi != elem_v.index:
        elem_v.pi = findSet(graph, elem_v.pi)

    return elem_v.pi


def union(graph: Dict[K, Edge], x, y):
    elem_x = Optional[Edge]
    elem_y = Optional[Edge]
    elem_x, elem_y = (graph[x], graph[y])

    if elem_x.s < elem_y.s:
        elem_x.pi = y
        elem_y.s += elem_x.s
    else:
        elem_y.pi = x
        elem_x.s += elem_y.s
