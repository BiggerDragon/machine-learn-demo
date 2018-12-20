import numpy as np

print('字符串函数')

print('向量化字符串操作')
print('连接两个字符串')
print(np.char.add(['hello'], ['xyz']))
print('\n')

print(np.char.add(['hello', 'hi'], ['abc', 'xyz']))

print('执行多重连接')
print(np.char.multiply('Hello', 3))

print(np.char.center('hello', 20, fillchar='*'))

print(np.char.capitalize('hello world'))

print(np.char.title('hello how are you?'))

print(np.char.lower(['HELLO', 'WORLD']))
print(np.char.lower('HELLO'))

print(np.char.upper(['hello','world']))
print(np.char.upper('hello'))


print(np.char.split('hello how are you?'))
print(np.char.split('YiibaiPoint,Heeee,eeee', sep=','))

print(np.char.splitlines('hello\nhow are you?'))
print(np.char.splitlines('hello\rhow are you?'))

print('返回数组的副本，一处开头和结尾的特定字符')
print(np.char.strip('ashok arora', 'a'))
print(np.char.strip(['arosa', 'admin', 'java'], 'a'))

print('char.join()返回一个字符串，其中单个字符由特定分隔符连接')
print(np.char.join(':', 'dmy'))
print(np.char.join([':','-'], ['dmy', 'ymd']))

print(np.char.replace('He is a good boy', 'is', 'was'))

print('用给定编码编码给定字符串')
a = np.char.encode('hello', 'cp500')
print(a)
print(np.char.decode(a, 'cp500'))

