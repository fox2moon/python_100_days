"""
列表
@Time : 2020/4/2 13:58
@Author: zhangqian
"""

# list1 = [1, 2, 3, 4, 5]
# list1.insert(0, 0)
# list1.append("3")
# list1.append([6, 7, 8])
# # list1.append(*[6, 7, 8])  # 只能接受一个参数
# print(list1)
# list1.extend("4")
# # list1.extend(1) # 会报错； extend被传入的参数必须是可迭代对象
# print(list1)
# list1 += [10, 20]
# print(len(list1))
# print(list1)

# fruits = ['grape', 'apple', 'strawberry', 'waxberry']
# fruits += ['pitaya', 'pear', 'mango']
# fruits2 = fruits[1:3]
# print(fruits2)
# fruits3 = fruits[-3:-1]
# print(fruits3)
# # 可以通过完整切片操作来复制列表
# fruits4 = fruits[:]
# print(fruits4)
# fruits5 = fruits[::-1]
# print(fruits5)

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
list2 = sorted(fruits)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(fruits, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(fruits, key=len)
print(list2)
print(list3)
print(list4)