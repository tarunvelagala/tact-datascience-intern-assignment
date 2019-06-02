import numpy as np

# Dot and Cross product
n = int(input())
m = np.array([input().split() for _ in range(n)], int)
x = np.array([input().split() for _ in range(n)], int)

res = np.dot(m, x)
print(res)

res = np.cross(m, x)
print(res)
