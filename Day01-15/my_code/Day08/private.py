"""
访问可见性
@Time : 2020/4/6 10:43
@Author: zhangqian
"""


class Test(object):
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print("__bar")


def main():
    test = Test('hello')
    # test.__bar()  # 'Test' object has no attribute '__bar'
    # print(test.__foo)  # 'Test' object has no attribute '__foo'
    '''Python并没有从语法上严格保证私有属性或方法的私密性，
        它只是给私有的属性和方法换了一个名字来妨碍对它们的访问，
        事实上如果你知道更换名字的规则仍然可以访问到它们'''
    test._Test__bar()
    print(test._Test__foo)


if __name__ == '__main__':
    main()
