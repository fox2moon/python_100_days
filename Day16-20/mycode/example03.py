# coding=gbk
"""
װ����
@Time : 2020/4/13 10:26
@Author: zhangqian
"""
from functools import wraps

'''�Ӻ����з��غ���'''


# def hi(name="yasoob"):
#     def greet():
#         return "now you are in the greet() function"
#
#     def welcome():
#         return "now you are in the welcome() function"
#
#     if name == "yasoob":
#         return greet
#     else:
#         return welcome
#
#
# print(hi())  # <function hi.<locals>.greet at 0x000002281FB5C708>
# a = hi()  # �������Ը�ֵ������
# print(a)  # <function hi.<locals>.greet at 0x000001D14DEAC708>
# print(a())

'''��������Ϊ����������һ������'''


# def hi():
#     return "hi yasoob!"
#
#
# def doSomethingBeforeHi(func):
#     print("I am doing some boring work before executing hi()")
#     print(func())
#
#
# doSomethingBeforeHi(hi)

'''��һ��װ����'''


# def a_new_decorator(a_func):
#     @wraps(a_func)
#     def wrapTheFunction():
#         print('1')
#         a_func()
#         print('3')
#     return wrapTheFunction
#
#
# @a_new_decorator
# def a_function_requiring_decoration():
#     print('2')
#
#
# a_function_requiring_decoration()
# print(a_function_requiring_decoration.__name__)

'''��������װ���� (������־)'''


# def logit(logfile='out.log'):
#     def logging_decorator(func):
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__+' was called'
#             print(log_string)
#             with open(logfile, 'a') as opend_file:
#                 opend_file.write(log_string+"\n")
#             return func(*args, **kwargs)
#         return wrapped_function
#     return logging_decorator
#
#
# @logit()
# def myfunc1():
#     pass
#
#
# @logit(logfile='func2.log')
# def myfunc2():
#     pass
#
#
# myfunc2()


''''''