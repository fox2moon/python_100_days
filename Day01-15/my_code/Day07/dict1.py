"""
字典 ：定义 使用
@Time : 2020/4/3 9:45
@Author: zhangqian
"""

# -----------定义----------
# 创建字典的字面量语法
mvp = {'name': 'James', 'age': 18, 'is_mvp': True}
print(mvp)
# 创建字典的构造器语法
items1 = dict(name='James', age=18, is_mvp=True)
# 通过zip函数将两个序列压成字典
items2 = dict(zip([1, 2, 3], [4, 5, 6]))
# 创建字典的推导式语法
items3 = {num: num*1 for num in range(5)}

print(items1)
print(items2)
print(items3)
# ------------使用---------

# 根据键取值
print(mvp['name'])
# get方法也是通过键获取对应的值但是可以设置默认值
print(mvp.get('age', 35))
print(mvp)
print(mvp.popitem())  # 返回并删除字典中的最后一对键和值
print(mvp)
print(mvp.clear())  # 删除字典内所有元素 不返回任何
print(mvp)
