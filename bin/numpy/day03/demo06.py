import numpy as np

print('算数平均值')
a = np.array([[1, 2, 3], [4,5,6], [7,8,9]])
print(a)
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

print('加权平均值average()')
a = np.array([1,2,3,4])
# 不指定权重时相当于mean函数
print(np.average(a))

wts = np.array([4,3,2,1])
print(np.average(a, weights=wts))
print('返回权重的和')
print(np.average(a, weights=wts, returned=True))

print('average 多维数组')
a = np.arange(6).reshape(3,2)
print(a)
wt = np.array([3,5])
print(np.average(a, axis=1, weights=wt, returned=True))

