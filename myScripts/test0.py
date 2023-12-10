from myScripts.utility_dir.graph_matrix_script import *


def main():
    graph = GraphMatrix()
    file = "adatok10"
    read_to_graph_matrix_from_file(graph, file)
    graph.display()


if __name__ == "__main__":
    main()
