import numpy as np


MIN_LEN = 5
MAX_LEN = 10


def print_string(param_str, column_count, row_count):
   
    len_str = len(param_str)

    if not (MIN_LEN<= len_str <= MAX_LEN):
        raise ('文字列は5文字以上10文字以下にしてください')

    if not (param_str.isalpha() and param_str.isascii()):
        raise ('文字列はa～z, A～Zにしてください。')

    result_str = ''
    for _ in range(column_count):
        result_str += param_str
    for _ in range(row_count):
        print(result_str)