# coding=gbk
"""
���߳�
@Time : 2020/4/16 15:35
@Author: zhangqian
"""
import glob
import os
import threading

from PIL.Image import Image

'''ͼƬ���������ͼ'''
PREFIX = 'thumbnails'


def generate_thumbnail(infile, size, format='PNG'):
    """����ָ��ͼƬ�ļ�������ͼ"""
    file, ext = os.path.splitext(infile)
    file = file[file.rfind('/') + 1:]
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(outfile, format)


def main():
    """������"""
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    for infile in glob.glob('images/*.png'):
        print(infile)
        # for size in (32, 64, 128):
        #     # �����������߳�
        #     threading.Thread(
        #         target=generate_thumbnail,
        #         args=(infile, (size, size))
        #     ).start()


if __name__ == '__main__':
    main()
