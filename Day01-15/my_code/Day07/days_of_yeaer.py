"""
练习5：计算指定的年月日是这一年的第几天。
@Time : 2020/4/3 15:10
@Author: zhangqian
"""


def is_leap_year(year):
    is_leap = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        is_leap = True
    return is_leap


def days_of_year(year, month, day):
    # 首先判断是否是闰年
    is_leap = is_leap_year(year)
    leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 闰年
    no_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap:
        days = sum(leap_year[:month-1])+day
    else:
        days = sum(no_leap_year[:month-1])+day
    return days


if __name__ == '__main__':
    year = int(input("请输入年："))
    month = int(input("请输入月："))
    day = int(input("请输入日："))
    print(days_of_year(year, month, day))
