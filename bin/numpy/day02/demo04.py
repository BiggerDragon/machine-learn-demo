import numpy as np

a = np.array([10,11,12,13,14,15,16,17])
b = a.reshape((2,2,2))
print(b)

# 将轴2放在轴0前，其他轴相对位置不变
print(np.rollaxis(b, 2))

# 将轴2滚动到轴1，轴1移动到轴2原来的位置

print('\n')
print(np.rollaxis(b,2,1))

# 交换数组的两个轴
a = np.arange(8).reshape(2,2,2)
print(a)

print(np.swapaxes(a, 2, 0))


