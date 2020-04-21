# coding=gbk
"""
迭代器和生成器
@Time : 2020/4/16 10:29
@Author: zhangqian
"""


'''生成器是语法简化版的迭代器 '''


def fib(num):
    """生成器"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


generator = fib(5)
for g in generator:
    print(g)


'''
生成器进化为协程。
生成器对象可以使用`send()`方法发送数据，发送的数据会成为生成器函数中通过`yield`表达式获得的值。这样，生成器就可以作为协程使用，协程简单的说就是可以相互协作的子程序。
'''


# def calc_avg():
#     """流式计算平均值"""
#     total, counter = 0, 0
#     avg_value = None
#     while True:
#         value = yield avg_value
#         total, counter = total + value, counter + 1
#         avg_value = total / counter
#
#
# gen = calc_avg()
# next(gen)
# print(gen.send(10))
# print(gen.send(20))
# print(gen.send(30))
