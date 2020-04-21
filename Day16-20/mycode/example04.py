# coding=gbk
"""
����������֪ʶ
@Time : 2020/4/14 16:35
@Author: zhangqian
"""
from abc import ABCMeta, abstractmethod

"""
��н����ϵͳ - ���ž���ÿ��15000 ����ԱÿСʱ200 ����Ա1800��н�����۶�5%���

ABCMeta��# ��ʾͬһ������
@abstractmethod �� ����@abc.abstractmethodװ�������ϸ�����������ʵ���������

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
        print('%s��н����%.2f' % (employee.name, employee.get_salary()))


if __name__ == '__main__':
    main()
