"""
元组的定义、使用
@Time : 2020/4/2 17:25
@Author: zhangqian
"""

t1 = ('001', 'James', 18,  True)
print(t1[0])
# t1[1] = 'J' # 会报错 元组不支持修改元素
print(t1)
# 将元组转换成列表
mvp = list(t1)
mvp[1] = 'J'  # 列表支持修改
print(mvp)
# 将列表转换成元组
t2 = tuple(mvp)
print(t2)
