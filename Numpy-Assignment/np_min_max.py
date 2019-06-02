import numpy as np

my_array = np.array([[2, 5],
                     [3, 7],
                     [1, 3],
                     [4, 0]])

print(np.min(my_array, axis=0))
print(np.min(my_array, axis=1))
print(np.min(my_array, axis=None))

print(np.max(my_array, axis=0))
print(np.max(my_array, axis=1))
print(np.max(my_array, axis=None))
