"""
练习1：英制单位英寸与公制单位厘米互换。
@Time : 2020/3/30 15:40
@Author: zhangqian
"""

length = float(input("请输入长度："))
unit = input("请输入单位：")
if unit in 'in' or unit in '英寸':
    print("%.2f英寸 = %.2f厘米" % (length, length*2.54))
elif unit in 'cm' or unit in '厘米':
    print("%.2f厘米 = %.2f英寸" % (length, length/2.54))
else:
    print("请检查单位是否有误！")
