import numpy as np


MIN_LEN = 5
MAX_LEN = 10


def print_string(param_str, column_count, row_count):
    """文字列を行と列に繰り返し出力する

    Args:
        param_str (_type_): 表示する文字列
        column_count (_type_): 列方向に文字列表示を繰り返す数
        row_count (_type_): 表放列に文字列表示を繰り返す数
    """
    len_str = len(param_str)

    if not (MIN_LEN <= len_str <= MAX_LEN):
        
        raise ('文字列は5文字以上10文字以下にしてください')

    if not (param_str.isalpha() and param_str.isascii()):
        raise ('文字列はa～z, A～Zにしてください。')

    result_str = ''
    """簡単な和の
    """
    for _ in range(column_count):
        result_str += param_str
    for _ in range(row_count):

        print(result_str)