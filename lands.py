import os
import numpy as np
import matplotlib.pyplot as plt

rows = 150
cols = 150

grid = np.zeros((rows, cols))

def create_island(grid):
    num_points = np.random.randint(10, 20)
    points = np.random.randint(30, 120, size=(num_points, 2))
    for i in range(rows):
        for j in range(cols):
            if np.any(np.linalg.norm(points - [i, j], axis=1) < 20):
                grid[i, j] = 1  # Суша
    return grid

def add_water(grid):
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 0:  # Море
                for x in range(max(0, i-1), min(rows, i+2)):
                    for y in range(max(0, j-1), min(cols, j+2)):
                        if grid[x, y] == 1:  # Суша
                            if np.random.rand() < 0.5:
                                grid[i, j] = 3  # Глубокое море
                            else:
                                grid[i, j] = 4  # Мелкое море
    return grid

def add_beach_and_vegetation(grid):
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 1:  # Суша
                for x in range(max(0, i-1), min(rows, i+2)):
                    for y in range(max(0, j-1), min(cols, j+2)):
                        if grid[x, y] in [3, 4]:  # Глубокое или мелкое море
                            grid[x, y] = 2  # Пляж
                if np.random.rand() < 0.6:
                    grid[i, j] = 5  # Трава
                if np.random.rand() < 0.3:
                    grid[i, j] = 6  # Деревья
                if np.random.rand() < 0.1:
                    grid[i, j] = 7  # Горы
    return grid

def add_volcano(grid):
    if np.random.rand() < 0.1:  # 10% вероятность появления вулкана
        volcano_x, volcano_y = np.random.randint(30, 120), np.random.randint(30, 120)
        for i in range(max(0, volcano_x-5), min(rows, volcano_x+6)):
            for j in range(max(0, volcano_y-5), min(cols, volcano_y+6)):
                if np.sqrt((i - volcano_x)**2 + (j - volcano_y)**2) < 5:
                    grid[i, j] = 8  # Вулкан
    return grid

def add_details(grid):
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 1:  # Суша
                if np.random.rand() < 0.05:
                    grid[i, j] = 9  # Скалы
    return grid

grid = create_island(grid)
grid = add_water(grid)
grid = add_beach_and_vegetation(grid)
grid = add_volcano(grid)
grid = add_details(grid)

fig, ax = plt.subplots(figsize=(12, 12))
cmap = plt.get_cmap('terrain')
cmap.set_under('darkblue')
cmap.set_over('red')
ax.imshow(grid, cmap=cmap, vmin=-0.5, vmax=9.5, interpolation='nearest')
ax.axis('off')

output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
plt.savefig(os.path.join(output_dir, 'improved_island_generation.png'), bbox_inches='tight')
plt.show()
