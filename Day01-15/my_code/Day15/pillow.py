"""
使用pillow操作图像
@Time : 2020/4/7 16:46
@Author: zhangqian
"""
from PIL import Image

image = Image.open('./res/drink.jpg')
size = 128, 128
# 缩略图
image.thumbnail(size)
image.show()
