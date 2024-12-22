import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform

points = np.array([
    [-1, 6],  # A
    [-1, -1],  # B
    [4, 7],  # C
    [6, 7],  # D
    [1, -1],  # E
    [-5, 3],  # F
    [-2, 3],  # P
])


def calculate_distance_matrix(points):
    return squareform(pdist(points))


def prim_mst(dist_matrix):
    n = len(dist_matrix)
    in_mst = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0
    total_weight = 0
    for _ in range(n):
        u = -1
        for v in range(n):
            if not in_mst[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        in_mst[u] = True
        total_weight += min_edge[u]

        for v in range(n):
            if dist_matrix[u][v] < min_edge[v] and not in_mst[v]:
                min_edge[v] = dist_matrix[u][v]
    return total_weight


def calculate_mst_length_with_lambda(λ):
    Q = np.array([2 - λ, 3])

    points_with_Q = np.vstack([points, Q])

    dist_matrix = calculate_distance_matrix(points_with_Q)

    mst_length = prim_mst(dist_matrix)
    return mst_length


def optimize_lambda():
    lambda_values = np.linspace(-10, 10, 200)
    mst_lengths = []

    for λ in lambda_values:
        mst_length = calculate_mst_length_with_lambda(λ)
        mst_lengths.append(mst_length)

    optimal_lambda = lambda_values[np.argmin(mst_lengths)]
    optimal_mst_length = min(mst_lengths)

    return optimal_lambda, optimal_mst_length


optimal_lambda, optimal_mst_length = optimize_lambda()

print(f"The optimal value of λ is: {optimal_lambda}")
print(f"The minimum MST length is: {optimal_mst_length}")

lambda_values = np.linspace(-10, 10, 200)
plt.plot(lambda_values, [calculate_mst_length_with_lambda(λ) for λ in lambda_values])
plt.xlabel('λ')
plt.ylabel('MST Length')
plt.title('MST Length vs. λ')
plt.grid(True)
plt.show()
