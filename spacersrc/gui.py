# spacersrc/gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
from spacersrc.analyzer import scan_and_format_directory, scan_directory
from spacersrc.visualizer import visualize_data

def select_directory():
    try:
        path = filedialog.askdirectory()
        if not path:
            raise ValueError("No directory selected.")
        data = scan_directory(path)
        if not data:
            raise ValueError("No data to visualize.")
        visualize_data(data, 
                       title='Disk Usage Visualization', 
                       max_label_length=30, 
                       figsize=(12, 8), 
                       cmap='viridis', 
                       base_fontsize=10)
    except ValueError as ve:
        messagebox.showerror("Error", f"ValueError: {ve}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def create_gui():
    root = tk.Tk()
    root.title("Disk Usage Analyzer")

    select_button = tk.Button(root, text="Select Directory", command=select_directory)
    select_button.pack(pady=20)

    root.mainloop()
