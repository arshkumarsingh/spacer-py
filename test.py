import matplotlib.pyplot as plt
from matplotlib import cm
import squarify

sizes = [50, 25, 25]
labels = ['A', 'B', 'C']

color_map = plt.get_cmap('viridis')
norm_sizes = [float(i) / max(sizes) for i in sizes]
colors = [color_map(value) for value in norm_sizes]

squarify.plot(sizes=sizes, label=labels, alpha=.8, color=colors)
plt.axis('off')
plt.show()
