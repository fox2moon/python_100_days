"""
多态
@Time : 2020/4/6 15:10
@Author: zhangqian
"""
from abc import abstractmethod, ABCMeta


class Pet(object, metaclass=ABCMeta):
    # 加上@abc.abstractmethod装饰器后严格控制子类必须实现这个方法
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):

    def make_voice(self):
        print("%s : 汪汪汪" % self._nickname)


class Cat(Pet):

    def make_voice(self):
        print("%s : 喵喵喵" % self._nickname)


def main():
    pets = [Dog('狗子'), Cat('kitty'), Dog('二狗')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()

