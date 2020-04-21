"""
练习1：定义一个类描述数字时钟。
@Time : 2020/4/6 10:57
@Author: zhangqian
"""
from time import sleep


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                if self._hour == 24:
                    self._hour = 0
                    self._minute = 0
                else:
                    self._hour += 1

    def show(self):
        return "%02d:%02d:%02d" % (self._hour, self._minute, self._second)


def main():
    clock = Clock(24, 59, 56)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()

