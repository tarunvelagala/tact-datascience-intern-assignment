import numpy as np

a = np.array([int(i) for i in range(1, 5)], float)
b = np.array([int(i) for i in range(6, 10)], float)

print(a+b)
print(np.add(a, b))

print(a-b)
print(np.subtract(a, b))

print(a*b)
print(np.multiply(a, b))

print(a/b)
print(np.divide(a, b))

print(a % b)
print(np.mod(a, b))

print(a**b)
print(np.power(a, b))
