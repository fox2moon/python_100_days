"""
练习3：输入三条边长，如果能构成三角形就计算周长和面积。
说明：通过边长计算三角形面积的公式叫做[海伦公式](https://zh.wikipedia.org/zh-hans/海伦公式)。
@Time : 2020/3/30 15:55
@Author: zhangqian
"""

a, b, c = input('请输入三角形的三个边长（用空格隔开）:').split(' ')
a = float(a)
b = float(b)
c = float(c)
if a + b > c and a + c > b and b + c > a:
    p = a + b + c
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("可以构成三角形，周长是%.2f,面积是%.2f" % (p, area))
else:
    print('不可以构成三角形！')
