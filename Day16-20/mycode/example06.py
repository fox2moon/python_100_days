# coding=gbk
"""
多线程
@Time : 2020/4/16 15:35
@Author: zhangqian
"""
import glob
import os
import threading

from PIL.Image import Image

'''图片处理成缩略图'''
PREFIX = 'thumbnails'


def generate_thumbnail(infile, size, format='PNG'):
    """生成指定图片文件的缩略图"""
    file, ext = os.path.splitext(infile)
    file = file[file.rfind('/') + 1:]
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(outfile, format)


def main():
    """主函数"""
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    for infile in glob.glob('images/*.png'):
        print(infile)
        # for size in (32, 64, 128):
        #     # 创建并启动线程
        #     threading.Thread(
        #         target=generate_thumbnail,
        #         args=(infile, (size, size))
        #     ).start()


if __name__ == '__main__':
    main()
