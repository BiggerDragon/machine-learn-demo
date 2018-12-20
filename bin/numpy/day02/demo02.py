# numpy数组上的迭代

import numpy as np

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原数组是:')
print(a);print('\n')

for x in np.nditer(a):
    print(x)

# 转置数组
b = a.T
print(b)

for x in np.nditer(b):
    print(x)

c = b.copy(order='C')
print(c)

for x in np.nditer(c):
    print(x)

c = b.copy(order='F')

print(c)
for x in np.nditer(c):
    print(x)


for x in np.nditer(a, order='F'):
    print(x)

for x in np.nditer(a, order='C'):
    print(x)

# nditer可选参数op_flags

print('\n')
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2*x
print('修改后的数据为:')
print(a)

for x in np.nditer(a, flags=['external_loop'], order = 'F'):
    print(x)


a2 = np.arange(0, 60, 5)
a2 = a2.reshape(3, 4)
print(a2)

print('========\n')
b2 = np.array([1, 2, 3, 4], dtype=int)
print(b2)
print('\n')
for x, y in np.nditer([a2, b2]):
    print('%d:%d' % (x, y))


