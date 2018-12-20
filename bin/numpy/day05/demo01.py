print('Matplotlib是python的绘图库')
from matplotlib import pyplot as plt
import numpy as np
print('pyplot()是matplotlib库中最重要的函数用于绘制2D数据')
print('y = 2x + 5')
x = np.arange(1, 11)
print(x)
y = 2 * x + 5
print(y)
plt.title('Matlpotlib demo')
plt.xlabel('x axis caption')
plt.ylabel('y axis caption')
# plt.plot(x, y)
plt.plot(x, y, 'ob')

plt.show()
