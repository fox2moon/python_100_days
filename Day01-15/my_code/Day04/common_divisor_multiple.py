"""
练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
@Time : 2020/3/31 9:36
@Author: zhangqian
"""

x = int(input("请输入第一位正整数："))
y = int(input("请输入第二位正整数："))
if x > y:
    x, y = y, x

for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print("%d和%d的最大公约数是%d" % (x, y, factor))
        print("%d和%d的最小公倍数是%d" % (x, y, x * y // factor))
        break





