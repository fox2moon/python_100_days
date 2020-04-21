"""
正则匹配手机号码
@Time : 2020/4/7 10:57
@Author: zhangqian
"""
import re


def main():
    # pattern = re.compile(r'\d{11}')
    pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    pattern = re.compile('15600998765')
    sentence = '''
        重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
        不是15600998765，也是110或119，王大锤的手机号才是15600998765。
        '''
    # 查找所有匹配并保存到一个列表中
    num_list = re.findall(pattern, sentence)
    print(num_list)

    # 通过迭代器取出匹配对象并获得匹配的内容
    for res in pattern.finditer(sentence):
        print(res.group())

    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    main()
