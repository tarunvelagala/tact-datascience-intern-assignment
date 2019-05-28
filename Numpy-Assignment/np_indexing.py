import numpy as np

lst = [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8]]

a = np.array(lst, dtype='float')
print(a[:2, :2])

# Create a boolean ND array from the given array
b = a > 4
print(b)

# print the array satisfying the boolean condition
print(a[b])

# reverse the rows and array
print(a[::-1, ])

# Reverse the row and column positions
print(a[::-1, ::-1])
