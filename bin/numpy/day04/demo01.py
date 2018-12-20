import numpy as np
print('排序')

a = np.array([[3,7], [9, 1]])
print(a)
print(np.sort(a))

print(np.sort(a, axis=0))

dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([('raju', 21), ('anil', 25),('ravi', 17),('amar', 27)], dtype=dt)
print(a)
print('按照name排序')
print(np.sort(a, order='name'))

x = np.array([3,1,2])
print(x)
y = np.argsort(x)
print(y)
print(x[y])
print('使用虚幻重构原数组')
for i in y:
    print(x[i])


