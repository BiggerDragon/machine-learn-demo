from sklearn.datasets import load_iris
from numpy import tile
import operator

print("鸢尾花数据集实验...")
data = load_iris()
print("KNN算法实现...")
# 标签列表
labels = data.target
# 标签名列表
label_names = data.target_names
# 鸢尾花数据列表
iris = data.data


def KNN(k, data_set, labels1, x):


    """
    KNN算法实现方法
    :param k: 为统计前多少个数据类的数量
    :param data_set: 数据集
    :param labels1: 标签集
    :param x: 用户需要预测的对象(一个鸢尾花数据向量)
    :return:
    """

    # 1.计算向量x到向量data_set的欧式距离
    data_set_len = len(data_set)
    distance = tile(x, (data_set_len, 1)) - data_set
    distance = distance ** 2
    # 每行相加
    distance = distance.sum(axis=1)
    distance = distance ** 0.5

    # 2.排序计算出的欧氏距离列表,得到从小到大排序的索引
    sorted_index = distance.argsort()

    # 3.统计前k个数据类的数量
    class_count = {}
    for i in range(k):
        label = labels1[sorted_index[i]]
        class_count[label] = class_count.get(label, 0) + 1

    # 4.按照统计结果降序排列
    print("class_count:", class_count)
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    print("sorted_class_count:", sorted_class_count)
    # 5.返回结果
    return sorted_class_count[0][0]


def KNN_test():
    # 取所有数据测试
    test_ratio = 0.1
    row = len(iris)
    print("row", row)
    test_num = int(row * test_ratio)
    print("test_num", test_num)
    # 错误的个数
    error = 0.0
    for i in range(test_num):
        result = KNN(5, iris[test_num:row], labels, iris[i])
        print("返回的结果是:%s=>%s, 真实结果是:%s=>%s" %
              (result, label_names[result], labels[i], label_names[labels[i]]))
        if result != labels[i]:
            error += 1.0

    print("错误率为:%f" % (error / float(test_num)))


iris_instance = [6, 3, 4, 1]

result1 = KNN(5, iris, labels, iris_instance)
