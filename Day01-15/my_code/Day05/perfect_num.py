"""
找出10000以内的**完美数**。
完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身
如：6 6=1+2+3
@Time : 2020/3/31 14:35
@Author: zhangqian
"""
res = []
for n in range(1, 10000):
    # 先获取真因子
    total = 0
    factor = [y for y in range(1, n) if n % y == 0]
    # print("列表元素为: ", factor)
    for i in range(0, len(factor)):
        total = total + factor[i]
    # print("列表元素之和为: ", total)
    if n == total:
        print("%d是完美数" % n)
        res.append(n)





