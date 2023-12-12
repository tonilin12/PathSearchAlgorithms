import heapq
from typing import Optional, Any

from myScripts.utility_dir.CustomTypes import *


def apply_kruskal(Vertex_dict: Dict[Any, Vertex]):
    vertex_set = []

    for Vertex in Vertex_dict.values():
        make_set(Vertex)

    k = len(Vertex_dict)
    min_queue = []

    for Vertex in Vertex_dict.values():
        node: Optional[NeighbourNode]
        node = Vertex.neighbours
        while node:
            vertex = (Vertex.index, node.index)
            heapq.heappush(min_queue, (node.weight, vertex))

            node = node.next

    while k > 1 and min_queue:
        weight, vertex = heapq.heappop(min_queue)
        print("out: ", weight, "|", vertex)

        u_k, v_k = vertex

        x = findSet(Vertex_dict, u_k)
        y = findSet(Vertex_dict, v_k)

        if x != y:
            union(Vertex_dict, x, y)
            vertex_set.append(vertex)

            k = k - 1

    print(vertex_set)
    print()
    print()
    return vertex_set


def make_set(vertex: Optional[Vertex]):
    vertex.s = 1
    vertex.pi = vertex.index


def findSet(graph: Dict[Any, Vertex], v):
    elem_v: Optional[Vertex]
    elem_v = graph[v]

    if elem_v.pi != elem_v.index:
        elem_v.pi = findSet(graph, elem_v.pi)

    return elem_v.pi


def union(graph: Dict[Any, Vertex], x, y):
    elem_x = Optional[Vertex]
    elem_y = Optional[Vertex]
    elem_x, elem_y = (graph[x], graph[y])

    if elem_x.s < elem_y.s:
        elem_x.pi = y
        elem_y.s += elem_x.s
    else:
        elem_y.pi = x
        elem_x.s += elem_y.s
