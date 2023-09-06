# 随机生成密码
def random_mi_ma():
    """随机生成密码"""
    import string
    import random
    digits = string.digits
    ascii_lowercase = string.ascii_lowercase
    ascii_uppercase = string.ascii_uppercase
    punctuation = r"""!"#$&'()*+,-.:;=@_`~"""
    password_ = string.digits + ascii_lowercase + ascii_uppercase + punctuation
    try:
        pd_ipt = int(''.join(input("""请按照提示规则输入数字：
            1.最高等级密码：数字+大小写英文字母+符号
            2.日常平常密码：数字+大小写英文字母
            3.简单密码：数字+大写英文字母
            4.简单密码：数字+小写英文字母
            5.最低等级密码：大写英文字母
            6.最低等级密码：小写英文字母
            7.最低等级密码：数字
        """))[-1])  # 只取最后一位
        try:
            range_password = int(input("输入需要的密码个数："))
            if int(pd_ipt) == 1:
                print("Your password is: " + ''.join(random.choice(password_) for _ in range(range_password)))
            elif int(pd_ipt) == 2:
                print("Your password is: " + ''.join(
                    random.choice(digits + ascii_uppercase + ascii_lowercase) for _ in range(range_password)))
            elif int(pd_ipt) == 3:
                print(
                    "Your password is: " + ''.join(
                        random.choice(digits + ascii_uppercase) for _ in range(range_password)))
            elif int(pd_ipt) == 4:
                print(
                    "Your password is: " + ''.join(
                        random.choice(digits + ascii_lowercase) for _ in range(range_password)))
            elif int(pd_ipt) == 5:
                print("Your password is: " + ''.join(random.choice(ascii_uppercase) for _ in range(range_password)))
            elif int(pd_ipt) == 6:
                print("Your password is: " + ''.join(random.choice(ascii_lowercase) for _ in range(range_password)))
            elif int(pd_ipt) == 7:
                print("Your password is: " + ''.join(random.choice(digits) for _ in range(range_password)))
        except Exception as e:
            print('{}'.format(e))
    except Exception as e:
        print('{}'.format(e))
