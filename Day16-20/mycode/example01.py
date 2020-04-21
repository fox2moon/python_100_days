# coding=gbk
"""
进阶
@Time : 2020/4/9 10:42
@Author: zhangqian
"""
import collections
import heapq
import itertools

'''生成式（推导式）的用法，生成式（推导式）可以用来生成列表、集合和字典。'''
# prices = {
#       'AAPL': 191.88,
#       'GOOG': 1186.96,
#       'IBM': 149.24,
#       'ORCL': 48.44,
#       'ACN': 166.89,
#       'FB': 208.09,
#       'SYMC': 21.29
#   }
# # 用股票价格大于100元的股票构造一个新的字典
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)

'''嵌套列表 '''
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五个学生三门课程的成绩
# scores = [[None] * len(courses) for _ in range(len(names))]
# print(scores)
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] =float(input("请输入%s的%s成绩：" % (name, course)))
# print(scores)

"""heapq模块（堆排序）"""
# 从列表中找出最大的或最小的N个元素 堆结构(大根堆/小根堆)
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

'''`itertools` 迭代工具模块'''

# count = itertools.count(1)
# for i in count:
#     print(i)

'''`collections`模块'''
# 找出序列中出现次数最多的元素
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
