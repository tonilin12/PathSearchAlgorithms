from typing import Optional, Any

from myScripts.utility_dir.CustomTypes import *


def apply_berman_ford(graph_dict: Dict[Any, Vertex], start_point=None):
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
    start_point_elem.e = 0
    my_queue = []
    my_queue.append(start_point)
    negative_circle = []

    while my_queue:
        u = my_queue.pop()
        elem_u = graph_dict[u]
        if elem_u.pi is not None:
            result_list = [tup for tup in result_list
                           if tup[1] != elem_u.index]

            vertex = (elem_u.pi, elem_u.index)
            print(elem_u.pi, "->", elem_u.index, "d: ", elem_u.d)
            result_list.append(vertex)

        node: Optional[NeighbourNode]
        node = elem_u.neighbours

        while node:
            elem_v = graph_dict[node.index]

            if elem_v.d > elem_u.d + node.weight:
                elem_v.pi = elem_u.index
                elem_v.d = elem_u.d + node.weight
                elem_v.e = elem_u.e + 1
                if elem_v.e < len(graph_dict):
                    if elem_v.index not in my_queue:
                        my_queue.append(elem_v.index)
                else:
                    negative_circle = find_negative_circle(graph_dict, elem_v.index)

            node = node.next

    print("negative circile:", negative_circle)

    print(result_list)
    return result_list


def find_negative_circle(graph_dict: Dict[Any, Vertex], v):
    circle_Vertexs = []
    for index, Vertex in graph_dict.items():
        Vertex.b = False

    elem_v = graph_dict[v]
    elem_u = graph_dict[elem_v.pi]

    circle_Vertexs.append(elem_u.index)
    while not elem_u.b:
        elem_u.b = True
        elem_u = graph_dict[elem_u.pi]
        circle_Vertexs.append(elem_u.index)

    return circle_Vertexs
