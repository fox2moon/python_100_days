"""
继承
@Time : 2020/4/6 14:44
@Author: zhangqian
"""


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print("%s正在快乐的玩耍" % self._name)

    def watch_tv(self, age):
        if age >= 18:
            print("%s正在看猫和老鼠" % self._name)
        else:
            print("%s正在看泰坦尼克号" % self._name)


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print("%s的%s在学习%s" % (self._grade, self._name, course))


class Teacher(Person):
    def __init__(self, name, age, title):
        super(Teacher, self).__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print("%s%s正在教%s" % (self._name, self._title, course))


if __name__ == '__main__':
    student = Student('james', 15, '三年级')
    student.study("语文")
    teacher = Teacher('BoBo', 35, '教练')
    teacher.teach('basketball')
