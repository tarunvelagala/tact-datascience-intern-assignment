import numpy as np

my_array = [1, 2, 3, 4, 5, 6]

# create ND array
my_array = np.array(my_array)

# Reshape the array
my_array = my_array.reshape(2, 3)

# Transpose the array -> (3, 2)
print(my_array.transpose())

# Creates a flast list
print(my_array.flatten())
