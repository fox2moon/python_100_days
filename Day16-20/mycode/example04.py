# coding=gbk
"""
面向对象相关知识
@Time : 2020/4/14 16:35
@Author: zhangqian
"""
from abc import ABCMeta, abstractmethod

"""
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成

ABCMeta：# 表示同一类事物
@abstractmethod ： 加上@abc.abstractmethod装饰器后严格控制子类必须实现这个方法

"""


class Employee(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):

    def get_salary(self):
        return 15000.0


class Programer(Employee):

    def __init__(self, name, work_hour=0.0):
        self.work_hour = work_hour
        super(Programer, self).__init__(name)

    def get_salary(self):
        return 200.0 * self.work_hour


class salesman(Employee):
    def __init__(self, name, sales=0.0):
        self.sales = sales
        super(salesman, self).__init__(name)

    def get_salary(self):
        return 1800.0 + 0.05 * self.sales


class Employee_factory(object):
    @staticmethod
    def creaet_employee(emp_type, *args, **kwargs):
        all_emp_types = {'P': Programer, 'S': salesman, 'M': Manager}
        cls = all_emp_types[emp_type.upper()]
        return cls(*args, **kwargs) if cls else None


def main():
    emps = [
        Employee_factory.creaet_employee('M', 'James'),
        Employee_factory.creaet_employee('P', 'zhangqian', 10.0),
        Employee_factory.creaet_employee('S', 'xiaoma', 100.0)
    ]

    for employee in emps:
        print('%s的薪资是%.2f' % (employee.name, employee.get_salary()))


if __name__ == '__main__':
    main()
