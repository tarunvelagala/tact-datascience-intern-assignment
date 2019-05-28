import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])

# common items in the arrays
print(np.intersect1d(a, b))

# uncommon items in the arrays
print(np.setdiff1d(a, b))

# print index of matched items
print(np.where(a == b))
