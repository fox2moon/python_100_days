"""
读写二进制文件
@Time : 2020/4/6 18:05
@Author: zhangqian
"""


def main():
    try:
        with open('健身喝水.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('健身喝水2.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


if __name__ == '__main__':
    main()
