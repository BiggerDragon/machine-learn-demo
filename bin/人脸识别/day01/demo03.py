print('用scikit-image显示HOG图')
import matplotlib.pyplot as plt
from skimage import  color, io
from skimage.feature import hog
from skimage import data, exposure

img = io.imread('E:\data\pictures\zhu1.jpg')
print('img:')
print(img)
print('\n')
img = color.rgb2gray(img)
print(img)
print('\n')
print('type pf image is:{}'.format(type(img)))
print('image is:{}'.format(img))
print('no.of columns of image is:{}'.format(len(img[0])))
print('no.of rows of image is:{}'.format(len(img)))

array, hog_image = hog(img, orientations=9, pixels_per_cell=(8,8),
                       cells_per_block=(1,1), visualize=True, block_norm = 'L1')
fig, (ax1, ax2) =plt.subplots(1,2, figsize=(8,4))

ax1.imshow(img, cmap=plt.cm.gray)
ax1.set_title('imput image')

hog_img_rescaled = exposure.rescale_intensity(hog_image, in_range=(0,10))

print('hog_image:')
print(hog_image)
ax2.imshow(hog_img_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
plt.show()

