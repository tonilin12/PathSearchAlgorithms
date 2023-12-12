from myScripts.algorithm.FloydWarshall import *


def main():
    graph = GraphMatrix()
    file = "sorucefiles/adatok10"

    read_to_graph_matrix_from_file(graph, file)
    graph.display()
    apply_floyd_warshall(graph)
    graph.display()


if __name__ == "__main__":
    main()
