import numpy as np
print('线性代数')
print('dot:两个数组的点积')
a = np.array([[1,2], [3,4]])
b = np.array([[11,12],[13,14]])
print('[[1*11+2*13,1*12+2*14],[3*11+4*13, 3*12+4*14]')
print(np.dot(a, b))

print('vdot():返回两个向量的点积')
print('1*11 + 2*12 + 3*13 + 4*14')
print(np.vdot(a, b))

print('inner():返回一维数组的向量内积,对于更高维度他返回最后'
      '一个轴上的和的乘积')
print(np.inner(np.array([1,2,3]), np.array([0,1,0])))
print('1*0+2*1+3*0')

print('多维数组内积')
a = np.array([[1,2], [3,4]])
b = np.array([[11,12],[13,14]])
print(np.inner(a, b))
print('1*11+2*12, 1*13+2*14')
print('3*11+4*12, 3*13+4*14')

print('矩阵乘法')
a = [[1,2],[3,1]]
b = [[4,1],[2,2]]
print(np.matmul(a, b))
print(np.matmul(b, a))

a = [[1,0], [0,1]]
b = [1,2]
print('维度不一样')
print(np.matmul(a, b))
print(np.matmul(b,a))

print('维度大于2的数组')
a = np.arange(8).reshape(2,2,2)
b = np.arange(4).reshape(2,2)
print('a')
print(a)
print('b')
print(b)
print('\n')
print(np.matmul(a, b))

print('行列式')
print('linalg.det()')
a = np.array([[1,2], [3,4]])
print(np.linalg.det(a))

b = np.array([[6,1,1], [4,-2, 5], [2,8,7]])
print(b)
print(np.linalg.det(b))

print('linalg.solve() 给出矩阵形式的线性方程的解')
print('linalg.inv()计算矩阵的逆')
print('矩阵的逆乘于原始矩阵等于单位矩阵')
x = np.array([[1,2], [3,4]])
y = np.linalg.inv(x)
print(x)
print(y)
print(np.dot(x, y))

print('矩阵的逆')
a = np.array([[1,1,1], [0,2,5], [2,5,-1]])
print(a)
ainv = np.linalg.inv(a)
print(ainv)
b = np.array([[6],[-4], [27]])
print(b)
print(np.linalg.solve(a, b))
print(np.dot(ainv, b))





