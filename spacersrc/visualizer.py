# spacersrc/visualizer.py

import squarify
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn.preprocessing import MinMaxScaler
import os

def get_common_prefix(paths):
    # Convert all paths to lowercase to handle case sensitivity
    paths = [path.lower() for path in paths]
    return os.path.commonpath(paths)

def get_dynamic_fontsize(sizes, base_fontsize=10):
    # Calculate dynamic font size based on the size of each rectangle
    min_size = min(sizes)
    max_size = max(sizes)
    return [(size - min_size) / (max_size - min_size) * base_fontsize + base_fontsize for size in sizes]

def visualize_data(data, title='Data Visualization', max_label_length=30, 
                   figsize=(12, 8), cmap='viridis', base_fontsize=10):
    # Handle empty data
    if not data:
        print("The data dictionary is empty.")
        return
    
    sizes = list(data.values())
    labels = list(data.keys())
    
    # Remove entries with size 0
    sizes_labels = [(size, label) for size, label in zip(sizes, labels) if size > 0]
    if not sizes_labels:
        print("No non-zero sizes found to visualize.")
        return

    sizes, labels = zip(*sizes_labels)
    
    # Find common prefix and remove it from labels
    common_prefix = get_common_prefix(labels)
    labels = [os.path.relpath(label, common_prefix) for label in labels]
    
    # Normalize sizes to better visualize them
    total_size = sum(sizes)
    sizes = [size / total_size * 100 for size in sizes]
    
    # Create colors from a colormap with gradients
    color_map = plt.get_cmap(cmap)
    scaler = MinMaxScaler()
    norm_sizes = scaler.fit_transform([[size] for size in sizes])
    colors = [color_map(value[0]) for value in norm_sizes]
    
    # Shorten labels if they are too long
    labels = [label if len(label) <= max_label_length else label[:max_label_length] + '...' for label in labels]
    
    # Create dynamic font sizes
    font_sizes = get_dynamic_fontsize(sizes, base_fontsize)
    
    # Generate the rectangles
    rects = squarify.normalize_sizes(sizes, 100, 100)
    rects = squarify.squarify(rects, 0, 0, 100, 100)
    
    # Create a squarify plot with colors
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    for rect, label, color, font_size in zip(rects, labels, colors, font_sizes):
        x, y, dx, dy = rect['x'], rect['y'], rect['dx'], rect['dy']
        ax.add_patch(plt.Rectangle((x, y), dx, dy, facecolor=color, edgecolor="white", linewidth=2))
        # Ensure label fits within the rectangle
        if dx > 5 and dy > 5:  # Ensure the label fits comfortably within the rectangle
            ax.text(x + dx/2, y + dy/2, label, va='center', ha='center', fontsize=font_size, color='black', weight='bold', bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))
    
    # Add title
    plt.title(title, fontsize=16)
    
    # Remove axes
    plt.axis('off')

    # Add a legend
    sm = plt.cm.ScalarMappable(cmap=color_map, norm=plt.Normalize(vmin=0, vmax=total_size))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, orientation="horizontal", pad=0.1, aspect=50)
    cbar.set_label('Normalized Size', fontsize=12)

    plt.show()

# Example usage:
data = {
    'C:/path/to/dir/A': 10000000, 
    'C:/path/to/dir/B': 20000000, 
    'C:/path/to/dir/C': 0, 
    'C:/path/to/dir/D': 40000000
}
visualize_data(data, 
               title='Sample Data Visualization', 
               max_label_length=15, 
               figsize=(10, 6), 
               cmap='plasma', 
               base_fontsize=12)
