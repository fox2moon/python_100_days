# coding=gbk
"""
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
@Time : 2020/4/3 10:53
@Author: zhangqian
"""

import string
import random


def verifica_code(code_len=4):
    veri_code = ""
    letters = string.ascii_letters  # 获取所有的大小写字母
    # 大写string.ascii_uppercase
    # 小写string.ascii_lowercase
    numbers_list = ['%s' % num for num in range(0, 10)]  # 获取1-10
    numbers = ''.join(numbers_list)
    letters_number = letters + numbers
    for i in range(code_len):
        code = random.choice(letters_number)  # 选择任意一个字符
        veri_code += code
    return veri_code


def verifica_code2(code_len=4):
    # 从a-zA-Z0-9生成指定数量的随机字符：
    veri_code = ''.join(random.sample(string.ascii_letters + string.digits, code_len))
    return veri_code


if __name__ == '__main__':
    print(verifica_code())
    print(verifica_code2())
