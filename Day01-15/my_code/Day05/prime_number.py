"""
输出**100以内所有的素数**。
素数指的是只能被1和自身整除的正整数（不包括1）
@Time : 2020/3/31 15:58
@Author: zhangqian
"""
prime_num = []
for n in range(1, 100):
    prime = [i for i in range(1, n) if n % i == 0]
    # print(prime)
    if len(prime) == 1:
        prime_num.append(n)
print("100以内所有的素数: ", prime_num)


