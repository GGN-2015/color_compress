import os
import numpy as np
from PIL import Image

def png_maker(image_array, filepath):
    image = Image.fromarray(image_array, 'RGBA') # 从 NumPy 数组创建图像
    image.save(filepath)                         # 显示图像

def png_maker_usage(): # 带透明度的图像构建
    dirnow = os.path.dirname(os.path.abspath(__file__))
    width = 100
    height = 100
    channels = 4  # RGB 图像
    image_array = np.zeros((height, width, channels), dtype=np.uint8)
    image_array[:, :width//2] = [255, 0, 0, 128]  # 左侧区域为红色
    image_array[:, width//2:] = [0, 255, 0, 128]  # 右侧区域为绿色
    png_maker(image_array, os.path.join(dirnow, "test.png"))
