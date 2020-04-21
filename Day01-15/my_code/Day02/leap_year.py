"""
输入年份 如果是闰年输出True 否则输出False
@Time : 2020/3/30 15:12
@Author: zhangqian
"""

year = int(input("请输入年份："))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("%d是闰年" % year)
else:
    print("%d不是闰年" % year)