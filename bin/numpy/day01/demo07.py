import numpy as np

# 布尔索引
# 当结果对象是布尔运算(例如比较运算符)的结果时，
# 将使用此类型的高级索引

# 大于5的元素会作为布尔索引的结果返回

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('x数组:')
print(x)
print('\n')
# 打印出大于5的元素
print('大于5的元素是:')
print(x[x>5])

# 使用~(取补运算符)来过滤NaN
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])

# 从数组中过滤非复数元素
b = np.array([1, 2+6j, 5, 3.5+5j])
print(b[np.iscomplex(b)])


