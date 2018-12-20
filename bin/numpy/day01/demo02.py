import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.shape)

a.shape = (3, 2)
print(a)

b = a.reshape(1, 6)
print(b)

print(a.ndim)

a = np.arange(24)
print(a)
b = a.reshape(2, 4, 3)
print(b)
print(b.ndim)

print(b.itemsize)
a = np.array([1, 2, 3])
print(a.itemsize)

print(a.flags)



