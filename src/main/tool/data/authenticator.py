import re
import hmac
import hashlib
import base64
import struct
import time


class Authenticator(object):
    def __init__(self, secret):
        self.__secret = secret
        self.__time_interval = 120

    def def_check_totp(self, secret) -> str:
        hn = hmac.new(
            base64.b32decode(base64.b32encode(s=self.__secret.encode('utf-8')), True),
            struct.pack(">Q", int(time.time()) // self.__time_interval),
            hashlib.sha1).digest()
        ob = hn[19] & 15
        dynamic_passwd = str((struct.unpack(">I", hn[ob:ob + 4])[0] & 0x7fffffff) % 1000000)
        return str(0) + str(dynamic_passwd) if len(dynamic_passwd) < 6 else dynamic_passwd

    def id_card_verification(self, id_number) -> bool:
        """身份证校验
            身份证简单规则，举例：
            37               29          28      1999                       09          29          34          3     4
            第一位1-9第二位0-9 市辖区01-99 县01-99  年份:0-9 开头，后面三位数字0-9  月份0-1 0-9  日期0-3 0-9  前2位数字0-9 性别奇偶 最后一位为数字或X或x
            前六位地区，非0打头: [1-9]\d{5}
            出身年份，覆盖范围为 1800-3999 年: (18|19|([23]\d))\d{2}
            月份，01-12月: ((0[1-9])|(10|11|12))
            日期，01-31天: (([0-2][1-9])|10|20|30|31)
            顺序码三位 + 一位校验码: \d{3}[0-9Xx]

            15位的身份证：
            前六位地区，非0打头: [1-9]\d{5}
            出生年份后两位00-99: \d{2}
            月份，01-12月: ((0[1-9])|(10|11|12))
            日期，01-31天: (([0-2][1-9])|10|20|30|31)
            顺序码三位，没有校验码 \d{3}
            假设18位身份证号码:41000119910101123X  410001 19910101 123X
            ^开头
            [1-9] 第一位1-9中的一个      4
            \\d{5} 五位数字           10001（前六位省市县地区）
            (18|19|20)                19（现阶段可能取值范围18xx-20xx年）
            \\d{2}                    91（年份）
            ((0[1-9])|(10|11|12))     01（月份）
            (([0-2][1-9])|10|20|30|31)01（日期）
            \\d{3} 三位数字            123（第十七位奇数代表男，偶数代表女）
            [0-9Xx] 0123456789Xx其中的一个 X（第十八位为校验值）
            $结尾

            假设15位身份证号码:410001910101123  410001 910101 123
            ^开头
            [1-9] 第一位1-9中的一个      4
            \\d{5} 五位数字           10001（前六位省市县地区）
            \\d{2}                    91（年份）
            ((0[1-9])|(10|11|12))     01（月份）
            (([0-2][1-9])|10|20|30|31)01（日期）
            \\d{3} 三位数字            123（第十五位奇数代表男，偶数代表女），15位身份证不含X
            $结尾
            """

        if len(id_number) != 18 and len(id_number) != 15:
            print('身份证号码长度错误')
            return False
        regular_expression = "(^[1-9]\\d{5}(18|19|20)\\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\\d{3}[" \
                             "0-9Xx]$)|(^[1-9]\\d{5}\\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\\d{3}$)"

        if re.match(regular_expression, id_number):
            if len(id_number) == 18:
                n = id_number.upper()
                # 前十七位加权因子
                var = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
                # 这是除以11后，可能产生的11位余数对应的验证码
                var_id = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

                sum_ = 0
                for i in range(0, 17):
                    sum_ += int(n[i]) * var[i]
                sum_ %= 11
                if (var_id[sum_]) != str(n[17]):
                    print("身份证号规则核验失败，校验码应为", var_id[sum_], "，当前校验码是：", n[17])
                    return False
            return True
        else:
            return False

# secret = 'li'
# a = Authenticator(secret)
# time_interval = 120
# dq = int(time.time())
# xg = (dq // time_interval + 1) * time_interval - dq
# print(
#     f'用户{secret}的口令 {a.def_check_totp(secret)} 有效期为{xg if len(str(xg)) == 3 else str(xg).rjust(3, "0")}秒')

# while True:
#     secret = 'li'
#     time_interval = 120
#     dq = int(time.time())
#     xg = (dq // time_interval + 1) * time_interval - dq
#     print(
#         f'用户{secret}的口令 {a.def_check_totp(secret)} 有效期为{xg if len(str(xg)) == 3 else str(xg).rjust(3, "0")}秒')
#     time.sleep(1)
