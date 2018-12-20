import numpy as np
print('无复制')
a = np.arange(6)
print('我们的数组是:')
print(a)
print(id(a))
b = a
print(id(b))
b.shape = (3,2)
print(b)
print(a)

print('视图和浅复制')
a = np.arange(6).reshape(3,2)
print(a)
b = a.view()
print(b)

print(id(a))
print(id(b))
b.shape = 2, 3
print(b)
print(a)

a = np.array([[10,10],[2,3],[4,5]])
print(a)
print('创建切片')
s = a[:, :2]
print(s)
print(id(a))
print(id(s))

print('深复制')
b = a.copy()
print(b)
print(id(b))
print(id(a))
print(b is a)

b[0,0] = 100
print(b)
print(a)
