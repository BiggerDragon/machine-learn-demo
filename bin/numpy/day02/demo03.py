# numpy 数组操作
import numpy as np

a = np.arange(8)
print(a)

print('\n')

b = a.reshape(4, 2)
print(b)


a = np.arange(10).reshape(2, 5)
print(a)
print('\n')

print(a.flat[5])

print(a.flatten())

print(a.flatten(order='F'))
print(a.flatten(order="C"))

print(a.ravel())

print(a.ravel(order="F"))

# 转置数组
print(np.transpose(a))


