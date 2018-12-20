import numpy as np

print('添加元素或者删除元素')
print('resize返回指定大小的新数组')
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
b = np.resize(a, (3,2))
print(b)
print(b.shape)
b = np.resize(a,(3,3))
print(b)
print(b.shape)

print('append===在输入数组的末尾添加至，分配新的数组')
print('向数组中添加元素，两个参数都会被展开')
print(np.append(a, [7,8,9]))
print('\n')
print('沿0轴添加元素')
print(np.append(a,[[7,8,9]], axis=0))
print('沿轴1添加元素')
print(np.append(a, [[7,8,9], [10,11,12]], axis=1))

print('insert在给定索引之前沿给定轴输入数组中的插入值')
a = np.array([[1,2],[3,4],[5,6]])
print(a)
print(a.shape)
print('没有指定轴，数组将展开')
print(np.insert(a, 3, [11,12]))
print('传递axis参数，会广播值数组来匹配输入数组')
print('沿0轴广播')
print(np.insert(a, 1, [11], axis=0))
print('沿轴1广播')
print(np.insert(a, 1, 11, axis=1))

print('delete===返回输入数组中删除指定子数组的新数组')
a = np.arange(12).reshape(3,4)
print(a)
print('没有指定轴，删除元素后展开')
print(np.delete(a,5))
print('删除第二列')
print(np.delete(a, 1, axis=1))

print('包含从数组中删除的替代值的切片')
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.delete(a, np.s_[::2]))


print('unique返回数组中去重元素数组')
a = np.array([5,2,6,2,7,5,6,8,2,9])
print(a)
print('第一个数组的去重值')
u = np.unique(a)
print(u)
print('去重数组的索引数组')
u,indices = np.unique(a, return_index=True)
print(u)
print(indices)
print('原数组')
print(a)
print('==========================')
print('去重数组的下标')
u,indices = np.unique(a, return_inverse=True)
print(u)
print(indices)
print('使用下表重构原数组')
print(u[indices])

print('返回去重元素的重复数量')
u, indices = np.unique(a, return_counts=True)
print(u)
print(indices)






