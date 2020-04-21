"""
获取给定文件的后缀名
@Time : 2020/4/3 11:55
@Author: zhangqian
"""


def get_file_suffix(file, has_dot=False):
    suffix = file.split(".")[-1]
    if suffix and has_dot:
        suffix = '.' + file.split(".")[-1]
    print(suffix)
    return suffix


suffix = get_file_suffix("123.doc")
suffix = get_file_suffix("123.ppt", True)
