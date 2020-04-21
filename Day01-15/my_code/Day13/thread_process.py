"""
线程与进程
@Time : 2020/4/7 13:56
@Author: zhangqian
"""


# Python中的多进程
# from multiprocessing.context import Process
# from random import randint
# from time import time, sleep
#
#
# def download_file(filename):
#     start = time()
#     print("开始下载%s" % filename)
#     sleep(randint(3,5))
#     print("%s下载完成" % filename)
#     end = time()
#     print("下载%s花费了%.2f" % (filename, end-start))
#
#
# def main():
#     start = time()
#     p1 = Process(target=download_file, args=('1.doc',))
#     p1.start()
#     p2 = Process(target=download_file, args=('2.doc',))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
#
# if __name__ == '__main__':
#     main()


# Python中的多线程
from random import randint
from threading import Thread
from time import time, sleep


class download_task(Thread):
    def __init__(self, filename):
        super(download_task, self).__init__()
        self._filename = filename

    def run(self):
        start = time()
        print("开始下载%s" % self._filename)
        sleep(randint(3, 5))
        print("%s下载完成" % self._filename)
        end = time()
        print("下载%s花费了%.2f" % (self._filename, end-start))


def main():
    start = time()
    task1 = download_task('1.doc')
    task1.start()
    task2 = download_task('2.doc')
    task2.start()
    task1.join()
    task2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
