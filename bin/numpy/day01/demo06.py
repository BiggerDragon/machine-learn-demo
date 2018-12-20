import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])
# y中包含x中(0,0),(1,1),(2,0)位置处的元素
y = x[[0, 1, 2], [0, 1, 0]]
print(y)

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print('我们的数组时:')
print(x)
print('\n')

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])

# y中包含(0,0),(0,2),(3,0),(3,2)处的元素
y = x[rows, cols]
print('这个数组的每个角处的元素是:')
print(y)

z = x[1:4,1:3]
print(z)

