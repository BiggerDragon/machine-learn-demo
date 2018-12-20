import numpy as np

x = np.arange(9).reshape(1,3,3)
print(x)
y = np.squeeze(x)
print(y)
print(x.shape)
print(y.shape)

print('数组的连接')
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print('连个数组的维度相同')
print(np.concatenate((a,b)))
print('沿轴1连接')
print(np.concatenate((a,b), axis=1))

print('stack...')
a = np.array([[1,2],[3,4]])
print(a)
print('\n')
b = np.array([[5,6], [7,8]])
print(b)
print('\n')
print('沿轴0堆叠两个数组')
print(np.stack((a,b), 0))
print('沿轴1堆叠连个数组')
print(np.stack((a,b),1))

print('hstack===通过堆叠来生成水平单个数组')
print(np.hstack((a,b)))
print('vstack===通过堆叠来生成垂直单个数组')
print(np.vstack((a,b)))

