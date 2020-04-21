"""
输入一个正整数判断它是不是素数
素数指的是只能被1和自身整除的大于1的整数
@Time : 2020/3/30 18:16
@Author: zhangqian
"""
from math import sqrt

s = int(input("请输入一个数字："))
end = int(sqrt(s))
is_prime = True
for n in range(2, end+1):
    print(n)
    if s % n == 0:
        is_prime = False
        break
if is_prime and s != 1:
    print("%d是素数" % s)
else:
    print("%d不是素数" % s)




