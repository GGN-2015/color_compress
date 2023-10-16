from PIL import Image
import numpy as np

def png_reader(image_path): 
    image = Image.open(image_path) # 打开图像
    image = image.convert("RGBA")  # 将图像转换为 RGB 模式（如果图像不是 RGB 模式）
    width, height = image.size     # 获取图像的宽度和高度

    # 遍历每个像素并获取颜色
    pixel_colors = []
    for y in range(height):
        row_colors = []
        for x in range(width):
            r, g, b, a = image.getpixel((x, y))
            row_colors.append([r, g, b, a])

        pixel_colors.append(row_colors)

    # 返回所有像素的颜色列表
    return np.array(pixel_colors)

# 调用函数并传入图像路径
def png_reader_usage():
    image_path = r"C:\Users\Premier Bob\Pictures\Saved Pictures\Nacho摸头.png"
    colors = png_reader(image_path)
    print(colors.shape)
