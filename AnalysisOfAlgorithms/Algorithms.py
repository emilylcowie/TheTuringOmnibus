# "Rewrite the WALLPAPER algorithm to use not two colours (black and white) but three."

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, CSS4_COLORS

# Input values
cornerx = float(input("Enter the X-coordinate of the bottom-left corner: "))  
cornery = float(input("Enter the Y-coordinate of the bottom-left corner: "))  
side = float(input("Enter the side length of the square grid: ")) 

# Input colors
color_names = input("Enter the colors separated by commas (e.g., 'navy,blue,lightblue'): ").split(',')

# Validate and convert color names to hex codes
colors = []
for name in color_names:
    name = name.strip().lower()
    if name in CSS4_COLORS:
        colors.append(CSS4_COLORS[name])
    else:
        print(f"Warning: '{name}' is not a valid color name. Using default color 'black'.")
        colors.append('black')

# Create a grid
grid_size = 100
grid = np.ones((grid_size, grid_size))

# Iterate over the grid
for i in range(100):
    for j in range(100):
        # Calculate the center of each square
        x = cornerx + i * (side / 100)
        y = cornery + j * (side / 100)
        
        # Condition: create a pattern using modulo operation
        c = (x**2 + y**2) % len(colors)
        grid[i, j] = c

# Create a custom colormap with the user-specified colors
cmap = ListedColormap(colors)

# Plot the grid
plt.imshow(grid, cmap=cmap, interpolation="nearest")
plt.xticks([])  # Remove x-axis ticks
plt.yticks([])  # Remove y-axis ticks
plt.show()
