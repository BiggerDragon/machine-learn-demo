import numpy as np

print('numpy 算数运算')

a = np.arange(9, dtype=np.float_).reshape(3,3)
print(a)
b = np.array([10, 10, 10])
print(b)
print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.divide(a, b))

a = np.array([0.25, 1.33, 1, 0, 100])
print(np.reciprocal(a))

print('pytho处理整数除法的方式，对于绝对值大于1的整数元素')
print('始终位0')
b = np.array([100], dtype=int)
print(np.reciprocal(b))

a = np.array([10, 100, 1000])
print(np.power(a, 2))

b = np.array([1,2,3])
print(np.power(a, b))

a = np.array([10, 20, 30])
b = np.array([3, 5, 7])
print(np.mod(a, b))
print(np.remainder(a, b))

print('复数操作')

a = np.array([-5.6j, 0.2j, 11., 1+1j])
print(a)

print(np.real(a))
print(np.imag(a))
print(np.conj(a))
print('以角度制返回')
print(np.angle(a))



