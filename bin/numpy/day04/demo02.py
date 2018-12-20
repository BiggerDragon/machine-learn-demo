import numpy as np
print('使用键序列执行间接排序')
nm = ('raju', 'anil', 'ravi', 'amar')
dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
ind = np.lexsort((dv, nm))
print(ind)

print('使用这个索引来获取排序后的数据')
print([nm[i] + ", " + dv[i] for i in ind])

print('argmax() argmin()分别沿给定轴返回最大值和最小值的索引')
a = np.array([[30,40,70], [80,20,10], [50,90,60]])
print(a)
print(np.argmax(a))
print(a.flatten())

print('沿0轴的最大索引值')
maxindex = np.argmax(a, axis=0)
print(maxindex)
minindex = np.argmin(a)
print(minindex)
print(a.flatten()[minindex])
minindex = np.argmin(a, axis=0)
print(minindex)
minindex = np.argmin(a, axis=1)
print(minindex)


print('nonzero()... 返回数组中非零元素的索引')
a = np.array([[30,40,0], [0, 20, 10], [50, 0, 60]])
print(a)
print(np.nonzero(a))

print('where()返回数组中满足给定条件的元素的索引')
x = np.arange(9.).reshape(3,3)
print(x)
print(np.where(x>3))
y = np.where(x>3)
print(x[y])


print('extract()返回满足任何条件的元素')
condition = np.mod(x, 2) == 0
print('按元素的条件值')
print(condition)
print('使用条件提取元素')
print(np.extract(condition,x))


