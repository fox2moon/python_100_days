"""
1.华氏温度转换为摄氏温度。
提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。

@Time : 2020/3/30 14:51
@Author: zhangqian
"""

temp_huashi = float(input())
temp_sheshi = (temp_huashi-32)/1.8
print("%.2f华氏温度等于%.2f摄氏温度" % (temp_huashi, temp_sheshi))

