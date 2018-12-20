print('人脸探测和人脸标记')
print('将原图转换为HOG图片后，结合其他辅助技术')
print('比如线性分类器，影响金字塔和滚动窗口检查机制就可以')
print('生成人脸探测器')

print('线性分类器')
from skimage import io
import dlib

# 获取图片转换为数组
file_name = 'E:\data\pictures\zhu1.jpg'
image = io.imread(file_name)
print(image)
# 建立人脸探测器
detector = dlib.get_frontal_face_detector()
print('detector:', detector)
# 运行在图片数据上
detected_faces = detector(image, 1)
print('返现{}张人脸，与{}图片'.format(len(detected_faces),file_name))
# 人脸68点预测模型
model = "shape_predictor_68_face_landmarks.dat"
#提取特征
predictor = dlib.shape_predictor(model)
#建立窗口
win = dlib.image_window()
win.set_image(image)

for i, box in enumerate(detected_faces):
    win.add_overlay(box)
    print('第{}张人脸的位置:{},右边位置:{}.'.format(i, box.left, box.right))
    landmarks = predictor(image, box)
    print('landmarks:')
    print(landmarks)
    win.add_overlay(landmarks)
    dlib.hit_enter_to_continue()

