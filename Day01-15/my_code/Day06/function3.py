"""
练习3：实现判断一个数是不是素数的函数。
@Time : 2020/4/1 11:10
@Author: zhangqian
"""


def is_prime_number(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False


print(is_prime_number(6))

