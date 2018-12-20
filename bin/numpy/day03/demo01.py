import numpy as np

print('位操作')
print('bitwise_and===对输入数组中的整数的二进制表示的相应位执行位与运算')
print('13 和 17二进制形式')
a, b = 13, 17
print(bin(a))
print(bin(b))
print('\n')
print('13和17的位与')
print(np.bitwise_and(13,17))

print('bitwise_or==位或操作')
print(np.bitwise_or(13,17))
print(bin(np.bitwise_or(13,17)))

print('invert===计算位非对于有符号整数返回补码')
print('13的位反转，其中ndarray的dtype是uint8')
print(np.invert(np.array([13], dtype=np.uint8)))
print('\n')
print(bin(242))
print('13的二进制表示')
print(np.binary_repr(13, width=8))
print('242的二进制表示')
print(np.binary_repr(242, width=8))

print('left_shift左移')
print('将10的二进制左移两位')
print(np.left_shift(10, 2))
print('10的二进制')
print(np.binary_repr(10, width=8))
print('40的二进制表示')
print(np.binary_repr(40, width=8))


print('right_shift')
print('将40右移两位')
print(np.right_shift(40,2))




