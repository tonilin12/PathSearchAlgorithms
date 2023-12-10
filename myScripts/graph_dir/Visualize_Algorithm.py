import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate_graph(graph, sequence=None):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Set the layout for better visualization
    pos = nx.shell_layout(graph)

    # Draw the initial graph
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    # Function to update the plot during animation
    def update(num):
        ax.clear()

        # Draw the graph
        nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue',
                font_color='black')

        # Highlight the edges in blue
        highlighted_edges = [(a, b) for (a, b) in graph.edges() if (a, b) in sequence[:num + 1]]
        nx.draw_networkx_edges(graph, pos, edgelist=highlighted_edges, edge_color='blue', width=3.0)

        # Draw edge labels
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    # Create the animation
    if sequence != None:
        ani = FuncAnimation(fig, update, frames=len(sequence), interval=700, repeat=False)

    # Display the graph
    plt.show()
