import cv2 as cv
# print(cv)
# 读取图像，支持bmp,jpg,png,tiff等常用格式
img = cv.imread('E:\data\pictures\zhu1.jpg')
print(img)
# 创建窗口并显示图像
cv.namedWindow('zhuyoulong')
cv.imshow('zhuyoulong', img)
cv.waitKey(0)
# 释放窗口
cv.destroyAllWindows()


