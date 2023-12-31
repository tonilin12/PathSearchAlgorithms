from typing import Any

from myScripts.utility_dir.CustomTypes import *


def apply_dfs(graph_dict: Dict[Any, ColoredVertex], back_vertex=[]):
    result_list = []
    tuple_list = []

    time = 0
    for index, elem_u in graph_dict.items():
        if elem_u.color == Color.WHITE:
            time = dfs_visit(graph_dict, elem_u, time, result_list, tuple_list, back_vertex)

        print(elem_u.d, "/", elem_u.f, " Vertex:", index, "pi:", elem_u.pi)

        vertex = (elem_u.pi, elem_u.index)
        if elem_u.pi is not None:
            result_list.append(vertex)

        tuple_list.append((index, elem_u.f))

    tuple_list.sort(key=lambda x: x[1], reverse=True)
    topology_order = [item[0] for item in tuple_list]

    print("topology-order: ", tuple_list)
    print(result_list)
    print()
    print()

    return result_list, topology_order


def dfs_visit(graph_dict, elem_u, time, result_list,
              tuple_list, back_vertex=[]):
    elem_u.color = Color.GRAY
    time += 1
    elem_u.d = time

    v = elem_u.neighbours

    while v and (len(back_vertex) == 0):
        v_index = v.index
        elem_v = graph_dict[v_index]
        if elem_v.color == Color.WHITE:

            elem_v.pi = elem_u.index

            time = dfs_visit(graph_dict, elem_v, time, result_list, tuple_list, back_vertex)

        else:
            # print(elem_v.color)

            if elem_v.color is Color.GRAY:
                elem_v.pi = elem_u.index
                back_vertex.append(elem_v.index)

        v = v.next

    time += 1
    elem_u.f = time
    elem_u.color = Color.BLACK
    # back_Vertex.append("---")
    return time
