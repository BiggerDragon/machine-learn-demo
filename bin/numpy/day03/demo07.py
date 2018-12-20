import numpy as np
print('标准差')
print('标准差:与均值的偏差的平方的平均值的平方根')

a = np.array([1,2,3,4])
print(np.std(a))

print('方差')
print('方差是偏差平方的平均值')
print(np.var(a))
