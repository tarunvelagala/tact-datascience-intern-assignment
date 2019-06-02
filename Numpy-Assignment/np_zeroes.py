import numpy as np

# takes a tuple i.e shape of the array and creates array of all zeroes
a = np.zeros((2, 2))
print(a)

# takes a tuple i.e shape of the array and creates array of all float ones (1.) # [1., 1.]
b = np.ones((1, 2))
print(b)

# takes tuple and element to be filled i the array [[7.,7.], [7.,7.]]
c = np.full((2, 2), 7)
print(c)

# takes size of the array and produces identity matrix
d = np.eye(2)
print(d)
