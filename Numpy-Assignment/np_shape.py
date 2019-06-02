import numpy as np

a = np.array([1, 2, 3])  # 1D Array
print(a.shape)  # Shape -> for dimensions of the array

b = np.array([[1, 2, 3], [4, 5, 6]])  # 2D Array -> rows and columns
print(b.shape)

# Print the dimesion, size, shape of the array
print(a.ndim)
print(a.size)
print(a.dtype)


# reshape using np.shape
c = np.array([i for i in range(1, 7)])
c.shape = (3, 2)
print(c)

# reshape array to new nd array with shape (2, 3)
d = np.reshape(c, (2, 3))
print(d)

# reshape to one dimension
e = np.reshape(b, 6)
print(e)

# Infer one missing length from the other
f = np.reshape(b, (3, -1))
print(f)
