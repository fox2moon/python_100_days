"""
练习2：百分制成绩转换为等级制成绩。
**要求**：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
@Time : 2020/3/30 15:50
@Author: zhangqian
"""

s = float(input("请输入你的成绩："))
if s >= 90:
    print("你的等级是A")
elif 80 <= s < 90:
    print("你的等级是B")
elif 70 <= s < 80:
    print("你的等级是C")
elif 60 <= s < 70:
    print("你的等级是D")
else:
    print("你的等级是E")
