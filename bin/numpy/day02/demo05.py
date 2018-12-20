import numpy as np

# 修改维度

x = np.array([[1],[2],[3]])
y = np.array([4,5,6])

# 对y广播x
b = np.broadcast(x, y)

out = np.empty(b.shape)
print(out)
out.flat = [(u+v) for (u, v) in b]
print(out)

print('内建')
print(x + y)


# broadcast_to 将数字扩展到新形状
# 不连续，只是在原数组上返回只读视图

a = np.arange(4).reshape(1,4)

print(np.broadcast_to(a, (4,4)))

# expand_dims通过在指定位置插入新的轴来扩展数组的形状
x = np.array(([1,2],[3,4]))
print(x)
print('\n')
y = np.expand_dims(x, axis = 0)
print(y)
print(y.shape)
print(x.shape)

# 在位置1插入轴
y = np.expand_dims(x, axis=1)
print('在轴1处插入新轴')
print('x=')
print(x)
print('在轴1处插入新轴')
print(y)
print(y.shape)




