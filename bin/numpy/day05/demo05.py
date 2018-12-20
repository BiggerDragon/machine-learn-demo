import numpy as np
from matplotlib import pyplot as plt
print('绘制直方图')
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
np.histogram(a, bins=[0,20,40,60,80,100])
hist, bins = np.histogram(a, bins=[0,20,40,60,80,100])
print(hist)
print(bins)
plt.title('histogram')
plt.hist(a, bins)
plt.show()
