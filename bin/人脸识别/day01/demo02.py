import cv2
import numpy as np
#数字图像数据可以用矩阵来表示，因此可以采用矩阵理论和矩阵算法
# 对数字图像进行分析和处理。由于数字图像可以表示为矩阵的形式，
# 所以在计算机数字图像处理程序中，通常用二维数组来存放图像数据。
img = cv2.imread('E:\data\pictures\zhu1.jpg')
print('img:')
print(img)
print()
print('np.float32(img)/255.0')
im = np.float32(img)/255.0
print('im:')
print(im)

# 计算水平梯度和竖直梯度
gx = cv2.Sobel(im, cv2.CV_32F, 1, 0, ksize=1)
gy = cv2.Sobel(im, cv2.CV_32F,0, 1, ksize=1)
print('gx:')
print(gx)
print()
print('gy:')
print(gy)

