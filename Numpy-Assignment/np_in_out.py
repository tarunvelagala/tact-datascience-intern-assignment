import numpy as np

A = np.array([int(i) for i in range(20, 30)])
B = np.array([int(i) for i in range(50, 70)])

print(np.inner(A, B))

print(np.outer(A, B))
