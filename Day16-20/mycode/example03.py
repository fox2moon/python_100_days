# coding=gbk
"""
装饰器
@Time : 2020/4/13 10:26
@Author: zhangqian
"""
from functools import wraps

'''从函数中返回函数'''


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
# a = hi()  # 函数可以赋值给变量
# print(a)  # <function hi.<locals>.greet at 0x000001D14DEAC708>
# print(a())

'''将函数作为参数传给另一个函数'''


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

'''第一个装饰器'''


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

'''带参数的装饰器 (用于日志)'''


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