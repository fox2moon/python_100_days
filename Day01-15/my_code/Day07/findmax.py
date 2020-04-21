"""
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值
@Time : 2020/4/3 14:00
@Author: zhangqian
"""

def find_max_second(list):
    max, second = (list[0], list[1]) if list[0] > list[1] else (list[1], list[0])
    for i in range(2, len(list)):
        if max >= list[i] >= second:
            second = list[i]
        elif list[i] >= max:
            second = max
            max = list[i]
    print(max)
    print(second)


find_max_second([1, 2, 3, 4, 5])
