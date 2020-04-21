"""
练习1：在屏幕上显示跑马灯文字
@Time : 2020/4/3 10:22
@Author: zhangqian
"""
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        i = os.system('cls')  # os.system('clear') 清屏有问题
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()