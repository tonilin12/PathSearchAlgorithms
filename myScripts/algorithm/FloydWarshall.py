from myScripts.utility_dir.graph_matrix_script import *


def apply_floyd_warshall(graph: GraphMatrix):
    edge_dict = graph.edges
    negative_circles = []

    print()
    for vertex_k in edge_dict.keys():
        print("insert_vertex: ", vertex_k)
        for start_point in edge_dict.keys():
            for end_point in edge_dict.keys():
                edge_ij: Edge = edge_dict[start_point][end_point]
                edge_ik: Edge = edge_dict[start_point][vertex_k]
                edge_kj: Edge = edge_dict[vertex_k][end_point]

                condition1 = edge_ij.weight > edge_ik.weight + edge_kj.weight
                condition2 = len(negative_circles) == 0
                if condition2 and condition1:
                    print(start_point, "-", edge_ik.weight, "->", vertex_k
                          , "-", edge_kj.weight, "->", end_point)
        print("------------------------------------------------------")
