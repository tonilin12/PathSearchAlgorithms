from queue import Queue
from typing import Any

from myScripts.utility_dir.CustomTypes import *


def apply_bfs(graph_dict: Dict[Any, Vertex]):
    result_list = []
    travel_order = []
    source = list(graph_dict.keys())[0] if graph_dict else None
    start_point = graph_dict[source]
    my_queue = Queue()

    # setup first element of queue source from where BFS is starting
    node = start_point.neighbours
    start_point.d = 0
    my_queue.put(source)

    result_list.append(source)
    print("Vertex: ", source, "| d:", start_point.d, "| pi", start_point.pi)

    # loop goes until queue is empty
    while not my_queue.empty():

        # take out element from queue to process it
        u = my_queue.get()
        tail_Vertex = graph_dict[u]
        node = tail_Vertex.neighbours

        '''
            check neighbor of node and if its neighbour has 
            not been processed yet it put into queue to get processed
        '''
        while node:
            # nth neighbor of current element
            v = node.index
            elem_v = graph_dict[v]
            '''
                check if d has been set for the current destination
                check if the Vertex had been reached already
            '''

            if numpy.isinf(elem_v.d):
                '''
                    if the destination has not been reached yet 
                    set (destination d) to (source d) + 1
                    for example, the first iteration  
                    (destination d) will be (source d) + 1 = 0 + 1
                    that means we can reach that destination 
                    with 0 + 1 = 1 path length
                '''
                elem_v.d = tail_Vertex.d + 1
                elem_v.pi = u
                my_queue.put(v)
                result_list.append(v)
                print("Vertex: ", v, "| d:", elem_v.d, "| pi", elem_v.pi)
                vertex = (elem_v.pi, v)
                travel_order.append(vertex)

            # if everything is done proceed forward to the next neighbor
            node = node.next

    print(travel_order)
    print()
    return travel_order
