import numpy as np

a = np.arange(10)
s = slice(2, 7, 2)
print(a[s])

print(a[2:7:2])

print(a[2:])
print(a[2:5])

print('\n')
a = np.array([[1,2,3], [3,4,5], [4,5,6]])
print(a[...,1])
print(a[...,2])
print(a[1,...])
print(a[0,...])
print(a[...,1:])

