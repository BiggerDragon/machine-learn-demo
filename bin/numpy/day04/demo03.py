import numpy as np

print('numpy字节交换')
a = np.array([1, 256, 8755], dtype=np.int16)
print(a)
print('以十六进制表示内存中的数据')
print(map(hex, a))

