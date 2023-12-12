from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, font
from myScripts.algorithm.Dijkstra import *
from myScripts.utility_dir.Utility import *
from myScripts.graph_dir.graphfile import *

class GraphGUI:
    def __init__(self, master):
        self.master = master
        master.title("Dijkstra's Algorithm")
        master.geometry("400x200")  # Set a smaller initial size

        # Increase font size
        label_font = font.Font(size=12)
        entry_font = font.Font(size=12)

        self.source_label = Label(master, text="Enter startpoint:", font=label_font)
        self.source_label.grid(row=0, column=0)

        self.source_entry = Entry(master, font=entry_font, width=20)  # Adjust width
        self.source_entry.grid(row=0, column=1)

        self.dest_label = Label(master, text="Enter destination:", font=label_font)
        self.dest_label.grid(row=1, column=0)

        self.dest_entry = Entry(master, font=entry_font, width=20)  # Adjust width
        self.dest_entry.grid(row=1, column=1)

        # Adjust rowspan
        self.submit_button = Button(master, text="Submit", command=self.run_algorithm, font=label_font)
        self.submit_button.grid(row=2, column=0, columnspan=2)

    def run_algorithm(self):
        source = self.source_entry.get()
        destination = self.dest_entry.get()

        if not source or not destination:
            messagebox.showerror("Error", "Please enter both startpoint and destination.")
            return

        file = "sorucefiles/input"

        graph_raw = create_default_dict_from_file(file)

        cheapest_path_list = find_cheapest_path(graph_raw, source, destination)
        show_graph(graph_raw, cheapest_path_list)


if __name__ == '__main__':
    root = Tk()
    gui = GraphGUI(root)
    root.mainloop()
