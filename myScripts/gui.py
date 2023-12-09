import tkinter as tk
from tkinter import ttk
from subprocess import Popen
import sys


def start_animation(program_name):
    Popen([sys.executable, f"{program_name}.py"])


root = tk.Tk()
root.title("Animation Control")

# Create a style and configure the font for the button
style = ttk.Style()
style.configure("TButton", font=('Helvetica', 12))

# Program names and corresponding functions
programs = [
    ("BFS-traversal", "main_programs/main"),
    ("DFS-traversal", "main_programs/main2"),
    ("Prim traversal", "main_programs/main4"),
    ("Kruskal traversal", "main_programs/main5"),
    ("Dijkstra-traversal", "main_programs/main6"),
    ("Source/Desntination_DijkstraPath", "main_programs/main7")
    ,("DagShortestPath-traversal", "main_programs/main8")
     ,("QueueBermanFord-traversal", "main_programs/main9")
]

# Create buttons dynamically
for program_text, program_name in programs:
    # Determine the width based on the length of the button text
    button_width = max(len(f"Start {program_text}") + 4, 20)  # Set a minimum width of 20
    button = ttk.Button(
        root, text=f"Start {program_text}",
        command=lambda name=program_name: start_animation(name),
        width=button_width, style="TButton"
    )
    button.pack(pady=10)

root.mainloop()
