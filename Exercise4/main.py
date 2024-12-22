import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

points = []
for i in range(6):
    A = (1 - i, i - 1)
    B = (i, -i)
    C = (0, i)
    points.append(A)
    points.append(B)
    points.append(C)

points = np.array(points)

vor = Voronoi(points)

fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax=ax, show_vertices=False)

half_lines = 0
for ridge in vor.ridge_vertices:
    if -1 in ridge:
        half_lines += 1

plt.scatter(points[:, 0], points[:, 1], c='red', label='Points')
plt.legend()
plt.title('Voronoi Diagram and Half-Lines')
plt.grid(True)
plt.show()

print(f'Number of half-lines: {half_lines}')