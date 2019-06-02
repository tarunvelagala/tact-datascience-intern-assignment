import numpy as np

my_array = np.array([[1, 2, 3], [4, 5, 6]])

print(np.sum(my_array))

print(np.prod(my_array))

print(np.sum(my_array, axis=0))
print(np.sum(my_array, axis=1))
print(np.sum(my_array, axis=None))

print(np.product(my_array, axis=0))
print(np.product(my_array, axis=1))
