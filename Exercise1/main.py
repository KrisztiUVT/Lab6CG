import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, Delaunay

points = np.array([[3, -5], [-6, 6], [6, -4], [5, -5], [9, 10]])

vor = Voronoi(points)

delaunay = Delaunay(points)

fig, ax = plt.subplots(1, 2, figsize=(12    , 6))

ax[0].set_title('Voronoi Diagram')
ax[0].plot(points[:, 0], points[:, 1], 'ro')
ax[0].set_xlim(-10, 10)
ax[0].set_ylim(-10, 15)


for ridge in vor.ridge_vertices:
    if -1 not in ridge:
        ax[0].plot([vor.vertices[ridge[0]][0], vor.vertices[ridge[1]][0]],
                   [vor.vertices[ridge[0]][1], vor.vertices[ridge[1]][1]], 'b-')

ax[1].set_title('Delaunay Triangulation')
ax[1].plot(points[:, 0], points[:, 1], 'ro')

for simplex in delaunay.simplices:
    ax[1].plot([points[simplex[0], 0], points[simplex[1], 0]],
               [points[simplex[0], 1], points[simplex[1], 1]], 'g-')
    ax[1].plot([points[simplex[1], 0], points[simplex[2], 0]],
               [points[simplex[1], 1], points[simplex[2], 1]], 'g-')
    ax[1].plot([points[simplex[2], 0], points[simplex[0], 0]],
               [points[simplex[2], 1], points[simplex[0], 1]], 'g-')

plt.tight_layout()
plt.show()
