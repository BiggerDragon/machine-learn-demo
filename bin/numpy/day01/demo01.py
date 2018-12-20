import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.array([1, 2, 3, 4], dtype=complex)
print(b)

dt = np.dtype(np.int32)
print(dt)

print(np.int32)

print(np.dtype('i1'))
print(np.dtype('i2'))
print(np.dtype('i4'))

student = np.dtype([('name', 'S20'), ('age', np.int8), ('marks', np.int16)])
print(student)

a = np.array([('zhu', 20, 501), ('Fu', 21, 550)], dtype=student)
print(a)
print(a[0]['name'], ', ', a[1]['age'], ', ', a[1]['marks'])




