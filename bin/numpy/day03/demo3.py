import numpy as np
print('numpy 算数函数')
print('标准三角函数')
a = np.array([0, 30, 45, 60, 90])
print('不同角度的正玄值')
# 叫角度转换为弧度表示
print(np.sin(a*np.pi/180))
print('\n')
print('余弦值')
print(np.cos(a*np.pi/180))
print('\n')
print('正切值')
print(np.tan(a*np.pi/180))

print('反三角函数')
sin = np.sin(a*np.pi/180)
print(sin)
inv = np.arcsin(sin)
print(np.degrees(inv))

cos = np.cos(a*np.pi/180)
print(cos)
print(np.degrees(np.arccos(cos)))

tan = np.tan(a*np.pi/180)
print(np.degrees(np.arctan(tan)))


print('舍入函数')
a = np.array([1.0, 5.55, 123, 0.567, 25.532])
print(a)
print(np.around(a, decimals=1))
print(np.around(a))
print(np.around(a, 2))
print(np.around(a, -1))

a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print(a)
print(np.floor(a))

print(np.ceil(a))


