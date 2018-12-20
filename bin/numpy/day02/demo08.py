import numpy as np

print('数组分割')
print('split===沿特定轴将数组分为子数组')
a = np.arange(9)
print(a)
print('将数组分为三个大小相同的子数组')
b = np.split(a, 3)
print(b)
b = np.split(a, [4,7])
print('将数组在一维数组中表明的未知分割')
print(b)
print('hsplit水平分割')
a = np.arange(16).reshape(4,4)
b = np.hsplit(a,2)
print(b)
print('vsplit竖直分割')
print(np.vsplit(a, 2))


