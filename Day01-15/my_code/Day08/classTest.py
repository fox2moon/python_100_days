"""
定义类、创建和使用对象
@Time : 2020/4/6 10:10
@Author: zhangqian
"""


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s正在学习%s" % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print("%s正在看猫和老鼠" % self.name)
        else:
            print("%s正在看泰坦尼克号" % self.name)


def main():
    stu1 = Student('James', 8)
    stu1.watch_movie()


if __name__ == '__main__':
    main()

