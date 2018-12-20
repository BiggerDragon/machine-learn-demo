import numpy as np
print('numpy IO')
print('ndarray对象可以保存到磁盘文件中并可以从磁盘文件加载')
a = np.array([1,2,3,4,5])
np.save('outfile', a)
b = np.load('outfile.npy')
print(b)
