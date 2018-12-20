import numpy as np
from matplotlib import pyplot as plt
print('生成正弦波')
x = np.arange(0 ,3 * np.pi, 0.1)
print(x)
y = np.sin(x)
print(y)
plt.title('sine wave form')
plt.plot(x, y)
plt.show()
