import numpy as np
import os

from k_means    import k_means
from png_maker  import png_maker
from png_reader import png_reader

# 使用颜色聚类的方法对图像进行压缩
def color_compress(input_file, output_file, color_count=16):
    input_data = png_reader(input_file)
    
    # 把矩阵拍扁成向量：理论上由内置方法可以解决，懒得查了
    linear_data = []
    for i in range(input_data.shape[0]):
        for j in range(input_data.shape[1]):
            linear_data.append(input_data[i, j])
    linear_data = np.array(linear_data)

    # 计算聚类，四舍五入
    labels, centroids = k_means(linear_data, color_count)
    centroids = np.round(centroids)

    # 使用聚类中心替换同一类别中的元素
    compressed_data = []
    for i in range(input_data.shape[0]):
        row_data = []
        for j in range(input_data.shape[1]):
            idx = (i * input_data.shape[1]) + j
            row_data.append(centroids[labels[idx]])
        compressed_data.append(row_data)
    compressed_data = np.array(compressed_data, dtype=np.uint8)

    # 输出图像到 png 文件
    png_maker(compressed_data, output_file)

# 使用示例
def color_compress_usage():
    dirnow      = os.path.dirname(os.path.abspath(__file__))
    input_file  = os.path.join(dirnow, "img", "test_input.png")
    output_file = os.path.join(dirnow, "img", "test_output.png")
    color_compress(input_file, output_file, 16)
    print("DONE")