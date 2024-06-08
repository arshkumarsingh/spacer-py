# spacersrc/gui.py

import tkinter as tk
from tkinter import filedialog
from spacersrc.analyzer import scan_directory
from spacersrc.visualizer import visualize_data

def select_directory():
    path = filedialog.askdirectory()
    if path:
        data = scan_directory(path)
        visualize_data(data, 
                       title='Disk Usage Visualization', 
                       max_label_length=30, 
                       figsize=(12, 8), 
                       cmap='viridis', 
                       base_fontsize=10)

def create_gui():
    root = tk.Tk()
    root.title("Disk Usage Analyzer")

    select_button = tk.Button(root, text="Select Directory", command=select_directory)
    select_button.pack(pady=20)

    root.mainloop()
