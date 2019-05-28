import numpy as np

# sum of even and odd columns in the array
a = np.array([[2, 7, 12, 0], [3, 9, 3, 4], [4, 0, 1,  3]])

even_columns = a[:, ::2]

odd_columns = a[:, 1::2]

print(even_columns + odd_columns)
