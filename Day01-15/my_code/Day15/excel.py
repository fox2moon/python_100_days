# coding:utf-8
"""
@Time : 2020/4/7 17:48
@Author: zhangqian
"""
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

workbook = Workbook()
sheet = workbook.active
data = [
    [1001, '白元芳', '男', '13123456789'],
    [1002, '白洁', '女', '13233445566']
]
# sheet.append(["学号", "姓名", "性别", "手机号码"])
# sheet.append(["1", "2", "3", "4"])
sheet.append(["Fruit", "2011", "2012", "2013"])  # column headings must be strings 没解决
for row in data:
    sheet.append(row)
tab = Table(displayName="Table1", ref="A1:E5")

tab.tableStyleInfo = TableStyleInfo(
    name="TableStyleMedium9", showFirstColumn=False,
    showLastColumn=False, showRowStripes=True, showColumnStripes=True)
sheet.add_table(tab)
workbook.save('./res/全班学生数据.xlsx')

