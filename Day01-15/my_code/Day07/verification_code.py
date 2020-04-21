# coding=gbk
"""
��ϰ2�����һ����������ָ�����ȵ���֤�룬��֤���ɴ�Сд��ĸ�����ֹ��ɡ�
@Time : 2020/4/3 10:53
@Author: zhangqian
"""

import string
import random


def verifica_code(code_len=4):
    veri_code = ""
    letters = string.ascii_letters  # ��ȡ���еĴ�Сд��ĸ
    # ��дstring.ascii_uppercase
    # Сдstring.ascii_lowercase
    numbers_list = ['%s' % num for num in range(0, 10)]  # ��ȡ1-10
    numbers = ''.join(numbers_list)
    letters_number = letters + numbers
    for i in range(code_len):
        code = random.choice(letters_number)  # ѡ������һ���ַ�
        veri_code += code
    return veri_code


def verifica_code2(code_len=4):
    # ��a-zA-Z0-9����ָ������������ַ���
    veri_code = ''.join(random.sample(string.ascii_letters + string.digits, code_len))
    return veri_code


if __name__ == '__main__':
    print(verifica_code())
    print(verifica_code2())
