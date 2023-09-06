def alpha_to_num(alpha):
    """将字母字符串转换为数字"""
    num = 0
    for char in alpha:
        num = num * 26 + (ord(char) - ord('A') + 1)
    return num


def num_to_alpha(num):
    """将数字转换为字母字符串"""
    alpha = []
    while num > 0:
        num, remainder = divmod(num - 1, 26)
        alpha.append(chr(remainder + ord('A')))
    return ''.join(reversed(alpha))
