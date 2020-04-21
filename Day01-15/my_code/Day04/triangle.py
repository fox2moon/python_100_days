"""
练习3：打印如下所示的三角形图案。
@Time : 2020/3/31 10:06
@Author: zhangqian
"""
# row = int(input("请输入要打印三角形的行数："))
# for x in range(row):
#     # print("x: %d" % x)
#     for y in range(x+1):
#         # print("y: %d" % y)
#         print("*", end="")
#     print()


# row = int(input("请输入要打印三角形的行数："))
# for x in range(row):
#     for y in range(row):
#         if y < row-1-x:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()


row = int(input("请输入要打印三角形的行数："))
for x in range(row):
    for _ in range(row - x - 1):  # 打印空白
        print(" ", end="")
    for _ in range(2 * x + 1):
        print("*", end="")
    print()