import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

A = np.array([[5, -1], [7, -1], [9, -1], [7, -3], [11, -1], [-9, 3]])

A7 = np.array([3, 1])
A8 = np.array([6, -7])

points = np.vstack([A, A7, A8])

vor = Voronoi(points)

fig, ax = plt.subplots(figsize=(8, 8))
voronoi_plot_2d(vor, ax=ax, show_vertices=False)

ax.plot(A[:, 0], A[:, 1], 'ro', label='Original Points A1 to A6')
ax.plot(A7[0], A7[1], 'go', label='Point A7')
ax.plot(A8[0], A8[1], 'bo', label='Point A8')

for i, txt in enumerate(range(1, 7)):
    ax.annotate(f'A{txt}', (A[i, 0] + 0.1, A[i, 1] + 0.1))
ax.annotate('A7', (A7[0] + 0.1, A7[1] + 0.1))
ax.annotate('A8', (A8[0] + 0.1, A8[1] + 0.1))

ax.set_xlim([-15, 15])
ax.set_ylim([-15, 15])
ax.set_title("Voronoi Diagram with Points A1 to A8")

plt.legend()
plt.show()