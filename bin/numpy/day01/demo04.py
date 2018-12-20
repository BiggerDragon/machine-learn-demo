import numpy as np

x = [1, 2, 3]
print(x)

a = np.asarray(x)
print(a);print(type(a))

a = np.asarray(x, dtype=float)
print(a)

b = (3, 4, 5)
a = np.asarray(b)
print(a)

b = [(1, 2, 3),(4, 5)]
a = np.asarray(b)
print(a)

a = np.arange(10)
print(a)
a = np.arange(10, 20, 2)
print(a)

x = np.linspace(10, 20, 5)
print(x)

x = np.linspace(10, 20, 5, endpoint=False)
print(x)

x = np.linspace(10, 20, 5, retstep= True)
print(x)

x = np.linspace(10, 20, 5, endpoint=False, retstep=True)
print(x)
x = np.linspace(10, 20, 5, endpoint=True, retstep=True)
print(x)
