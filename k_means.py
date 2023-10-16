import numpy as np
from sklearn.cluster import KMeans

# dataset: 一个 n 行 m 列的矩阵，每行是一个元素，每列是一个特征
# k: 聚类的个数
def k_means(dataset, k, n_init=10):
    assert isinstance(dataset, np.ndarray)

    # 创建 KMeans 聚类模型，并拟合数据
    kmeans = KMeans(n_clusters=k, n_init=n_init)
    kmeans.fit(dataset)

    # 获取聚类结果，得到每个元素所在的类标以及每个类的中心坐标
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    return labels, centroids

# 教你如何使用 k_means 函数
def k_means_usage():
    X = np.array([[1, 2], [1, 3], [2, 3], [2, 4]]) # 输入了四个二维向量
    labels, centroids = k_means(X, 2)              # 进行二聚类
    print(labels)                                  # 输出四个整数，表示输入的四个向量各自的类标
    print(centroids)                               # 输出两个二维向量表示两个类的中心坐标