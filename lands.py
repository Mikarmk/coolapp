import os
import numpy as np
import matplotlib.pyplot as plt

rows = 50
cols = 50

grid = np.random.choice([0, 1], size=(rows, cols), p=[0.7, 0.3])  # 0 это море, 1 это суша

def apply_rules(grid):
    new_grid = grid.copy()
    for i in range(rows):
        for j in range(cols):
            neighbors = grid[max(0, i-1):min(rows, i+2), max(0, j-1):min(cols, j+2)]
            land_neighbors = np.sum(neighbors) - grid[i, j]
            if grid[i, j] == 1:
                if land_neighbors < 2:
                    new_grid[i, j] = 0
                elif land_neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if land_neighbors == 3:
                    new_grid[i, j] = 1
    return new_grid

for _ in range(10):
    grid = apply_rules(grid)

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(grid, cmap='ocean', interpolation='nearest')
ax.axis('off')

output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
plt.savefig(os.path.join(output_dir, 'islands.png'), bbox_inches='tight')
plt.show()
