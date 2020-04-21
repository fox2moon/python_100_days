"""
集合的定义 使用
1.不允许有重复元素，而且可以进行交集、并集、差集等运算
@Time : 2020/4/2 17:44
@Author: zhangqian
"""
set1 = {'1', 2, 3}
set1.add(4)
print(set1)
set1.pop()
print(set1)
set1.add(5)
print(set1)
set1.remove(5)
print(set1)
set1.discard(5)  # discard移除指定的集合元素 如果不存在 不会报错
# set1.remove(5)  # remove删除不存的,会报错
print(set1)


set2 = {'2', 2, 3}

print(set1 & set2)  # 交集
