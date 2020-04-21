"""
#### 练习1：实现计算求最大公约数和最小公倍数的函数。
@Time : 2020/4/1 9:46
@Author: zhangqian
"""


def gcd(x, y):
    """最大公约数"""
    if x > y:
        x, y = y, x
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def lcm(x, y):
    """最小公倍数"""
    if x > y:
        x, y = y, x
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i * (x // i) * (y // i)


# print(gcd(9, 8))
print(lcm(6, 9))
