"""
练习2：输入圆的半径计算计算周长和面积。
@Time : 2020/3/30 15:06
@Author: zhangqian
"""

r = float(input("输入圆的半径："))
perimeter = 2 * 3.14 * r
area = 3.14 * r * r
print("圆的半径是%d,周长是%.2f,面积是%.2f" % (r, perimeter, area))