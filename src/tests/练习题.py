import random

import pandas as pd


def to_excel(data):
    pd.DataFrame({'加减法公式': data}).to_excel('加减法公式.xlsx', index=False)


def generative_addition_subtraction(number):
    while True:
        start_big = random.randint(2, 99)
        end_small = random.randint(1, 100 - start_big)
        if start_big > end_small:
            addition_subtraction_list.add(f'{start_big} {random.choice("+-")} {end_small} =')
        else:
            addition_subtraction_list.add(f'{start_big} + {end_small} =')
        if len(addition_subtraction_list) >= number:
            to_excel(list(addition_subtraction_list))
            return


if __name__ == '__main__':
    addition_subtraction_list = set()
    BJ = True
    while BJ:
        number_int = input("请输入需要生成加减法的个数(正整数)，直接回车退出功能:")
        if number_int:
            number_int = int(number_int)
            if isinstance(number_int, int):
                generative_addition_subtraction(number_int)
        else:
            BJ = False
