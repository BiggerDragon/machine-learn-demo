import numpy as np
import numpy.matlib
print('矩阵库')
print(np.matlib.empty((2,2)))
print(np.matlib.zeros((2,2)))
print(np.matlib.ones((2,2)))
print('eye()返回一个矩阵对角线元素为1，其他位置为0')
print(np.matlib.eye(n=3,M=4,k=0, dtype=float))
print('单位矩阵:主对角线元素都为1')
print(np.matlib.identity(5,dtype=float))

print('rand()返回给定大小的填充随机值矩阵')
print(np.matlib.rand(3,3))

print('矩阵总是二维的,ndarray是一个n维数组')
i = np.matrix('1, 2;3,4')
print(i)
j = np.asarray(i)
print(j)
k = np.asmatrix(j)
print(k)

