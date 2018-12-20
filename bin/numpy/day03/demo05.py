import numpy as np
print('统计函数')
a = np.array([[3,7,5], [8,4,3], [2,4,9]])
print('沿指定轴返回最大值和最小值')
print(np.amin(a, 1))
print(np.amax(a, 1))
print(np.amin(a, 0))
print(np.amax(a, 0))

print('ptp()沿轴的值的范围(最大值-最小值)')
print('即该函数返回的是数组元素的最大值和最小值直接的差值（max(array) - min(array)')
print(np.ptp(a))
print(np.ptp(a, axis=1))
print(np.ptp(a, axis=0))
print(a.shape)

print('percentile()===表示小于这个值得观察值占某个百分比')
a = np.array([[30,40,70],[80,20,10],[50,90,60]])
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=1))

print('中值,将数据样本的上半部分与下半部分分开的值')
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))





