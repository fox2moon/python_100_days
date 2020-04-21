"""
文件的读写
@Time : 2020/4/6 17:20
@Author: zhangqian
"""


def main():
    try:
        with open('自语.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')


if __name__ == '__main__':
    main()