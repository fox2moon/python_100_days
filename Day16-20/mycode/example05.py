# coding=gbk
"""
��������������
@Time : 2020/4/16 10:29
@Author: zhangqian
"""


'''���������﷨�򻯰�ĵ����� '''


def fib(num):
    """������"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


generator = fib(5)
for g in generator:
    print(g)


'''
����������ΪЭ�̡�
�������������ʹ��`send()`�����������ݣ����͵����ݻ��Ϊ������������ͨ��`yield`���ʽ��õ�ֵ���������������Ϳ�����ΪЭ��ʹ�ã�Э�̼򵥵�˵���ǿ����໥Э�����ӳ���
'''


# def calc_avg():
#     """��ʽ����ƽ��ֵ"""
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
