# coding=gbk
"""
����
@Time : 2020/4/9 10:42
@Author: zhangqian
"""
import collections
import heapq
import itertools

'''����ʽ���Ƶ�ʽ�����÷�������ʽ���Ƶ�ʽ���������������б����Ϻ��ֵ䡣'''
# prices = {
#       'AAPL': 191.88,
#       'GOOG': 1186.96,
#       'IBM': 149.24,
#       'ORCL': 48.44,
#       'ACN': 166.89,
#       'FB': 208.09,
#       'SYMC': 21.29
#   }
# # �ù�Ʊ�۸����100Ԫ�Ĺ�Ʊ����һ���µ��ֵ�
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)

'''Ƕ���б� '''
# names = ['����', '�ŷ�', '����', '��', '����']
# courses = ['����', '��ѧ', 'Ӣ��']
# # ¼�����ѧ�����ſγ̵ĳɼ�
# scores = [[None] * len(courses) for _ in range(len(names))]
# print(scores)
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] =float(input("������%s��%s�ɼ���" % (name, course)))
# print(scores)

"""heapqģ�飨������"""
# ���б����ҳ����Ļ���С��N��Ԫ�� �ѽṹ(�����/С����)
# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#       {'name': 'IBM', 'shares': 100, 'price': 91.1},
#       {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#       {'name': 'FB', 'shares': 200, 'price': 21.09},
#       {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#       {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#       {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
# print(heapq.nlargest(3, list2, key=lambda x: x['price']))
# print(heapq.nsmallest(3, list2, key=lambda x: x['price']))

'''`itertools` ��������ģ��'''

# count = itertools.count(1)
# for i in count:
#     print(i)

'''`collections`ģ��'''
# �ҳ������г��ִ�������Ԫ��
# words = [
#       'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
#       'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
#       'look', 'into', 'my', 'eyes', "you're", 'under'
# ]
# counter = collections.Counter(words)
# common = counter.most_common()
# print(common)
# print(counter.most_common(1))
# print(counter.most_common(0))
