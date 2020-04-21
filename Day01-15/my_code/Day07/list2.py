"""
列表 ： 生成式和生成器
@Time : 2020/4/2 15:59
@Author: zhangqian
"""

# 生成式
import sys

list1 = [x for x in range(10)]
print(list1)
list2 = [x + y for x in range(10) for y in range(10)]
print(list2)

# 生成器 generator
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 10))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
print(f)
for val in f:
    print(val)




