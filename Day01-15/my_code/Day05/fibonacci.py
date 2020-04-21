"""
1. 生成**斐波那契数列**的前20个数。
@Time : 2020/3/31 14:14
@Author: zhangqian
"""

s = int(input("请输入你生成斐波那契数列的前几个数："))
fib = []
fib.append(1)
fib.append(1)
for i in range(s):
    if i > 1:
        fib_new = fib[i-1]+fib[i-2]
        fib.append(fib_new)
print(fib)
