import numpy as np

x = np.empty([3, 2], dtype=int)
print(x)

z = np.zeros(5)
print(z)
z = np.zeros(5, dtype=int)
print(z)

z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)

o = np.ones(3)
print(o)

o = np.ones((2, 2), dtype=int)
print(o)


# 默认底数为10
a = np.logspace(1.0, 2.0, num=10)
print(a)

a = np.logspace(1, 10, num=10, base=2)
print(a)





