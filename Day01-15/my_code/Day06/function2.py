"""
练习2：实现判断一个数是不是回文数的函数。
@Time : 2020/4/1 10:19
@Author: zhangqian
"""
import math


def is_palindrome(num):
    """判断是否是回文数"""
    if num > 0:
        num_str = str(num)
        for i in range(math.floor(int(len(num_str))/2), 0, -1):
            if num_str[i] != num_str[-i-1]:
                return False
        return True


def is_palindrome2(x):
    str_x = str(x)
    return str_x == str_x[::-1]


print(is_palindrome(1231))
# print(is_palindrome2(123421))
