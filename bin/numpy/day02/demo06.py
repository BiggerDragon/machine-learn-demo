import numpy as np

# expand_dims
# 测试一维数组
x = np.array([1,2,3])
print(x)
print(x.shape)
y = np.expand_dims(x, 0)
print(y)
print(y.shape)

y = np.expand_dims(x, 1)
print(y)
print(y.shape)

y = np.expand_dims(x, 3)
print(y)
print(y.shape)

print('测试二维数组')
x = np.array([[1,2,3], [4,5,6]])
print(x)
print(x.shape)

y = np.expand_dims(x, 0)
print(y)
print(y.shape)

y = np.expand_dims(x, 1)
print(y)
print(y.shape)

