import numpy as np

# Simple 1D Array
a = np.array([1, 2, 3, 4, 5])
print(a)

# Float 1D Array => [1.,2.,3.,4.,5.]
b = np.array([1, 2, 3, 4, 5], float)
print(b)

# Complex 1D Array => [1.+ 0.0j,2.+ 0.0j,3.+ 0.0j,4.+ 0.0j,5.+ 0.0j]
c = np.array([1, 2, 3, 4, 5], dtype=complex)
print(c)

# Create ND array of minimum dimensions
d = np.array([1, 2, 3, 4, 5], ndmin=2)
print(d)

# Upcasting => Array of floats
e = np.array([1, 2, 3.0, 4.0, 5])
print(e)

# Vector or Array using arange
f = np.arange(4, dtype=np.int64)
print(f)
