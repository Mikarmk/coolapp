import os
import numpy as np
import matplotlib.pyplot as plt

rows = 150
cols = 150

grid = np.zeros((rows, cols)) 

def create_island(grid):
    num_points = np.random.randint(5, 15)  # Количество точек для определения формы острова
    points = np.random.randint(30, 120, size=(num_points, 2))  # Случайные точки для формирования острова
    for i in range(rows):
        for j in range(cols):
            if np.any(np.linalg.norm(points - [i, j], axis=1) < 20):  # Расстояние до ближайшей точки
                grid[i, j] = 1  # Суша
    return grid

def add_water(grid):
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 0:  # Море
                for x in range(max(0, i-1), min(rows, i+2)):
                    for y in range(max(0, j-1), min(cols, j+2)):
                        if grid[x, y] == 1:  # Суша
                            grid[i, j] = 3  # Глубокое море
    return grid

def add_beach_and_vegetation(grid):
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 1:  # Суша
                for x in range(max(0, i-1), min(rows, i+2)):
                    for y in range(max(0, j-1), min(cols, j+2)):
                        if grid[x, y] == 3:  # Глубокое море
                            grid[x, y] = 2  # Пляж
                        elif grid[x, y] == 0:  # Море
                            grid[x, y] = 4  # Мелкое море
                if np.random.rand() < 0.5:
                    grid[i, j] = 5  # Трава
                if np.random.rand() < 0.2:
                    grid[i, j] = 6  # Деревья
    return grid

grid = create_island(grid)

grid = add_water(grid)

grid = add_beach_and_vegetation(grid)

fig, ax = plt.subplots(figsize=(12, 12))
cmap = plt.get_cmap('terrain')
cmap.set_under('lightgray')
cmap.set_over('darkgreen')
ax.imshow(grid, cmap=cmap, vmin=-0.5, vmax=6.5, interpolation='nearest')
ax.axis('off')

output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
plt.savefig(os.path.join(output_dir, 'random_shaped_island.png'), bbox_inches='tight')
plt.show()
