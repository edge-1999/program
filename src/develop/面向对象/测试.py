import hmac
import hashlib
import base64
import struct
import time

# setup 1 : base32 secret
# 提示:Secret的长度最好不要超过32
Secret = 'username'

# Secret += '=' * (8-len(Secret)%8) # py3中base64模块要求字符串必须为8的倍数，不足部分使用 = 补全
# 在查阅相关资料时,发现解决【可以将Key进行b3decode】的代码都是这样写的(或者类似).
# 但是在生产环境中,为了给每个用户生成不一样的Key,我们必须通过各种算法,生成一个和用户有关的字符串作为Key使用,
# 如果你使用的是 Secret += '=' * (8-len(Secret)%8) 这种方式解决b32decode问题,那么当Key中有数字时,
# b32decode将会报错:binascii.Error: Non-base32 digit found,
# 通过测试,我找到了一段代替Secret += '=' * (8-len(Secret)%8)的代码,所以在我这篇文章中,
# 将会使用Secret = base64.b32encode(s=Secret.encode('utf-8'))来代替类似Secret += '=' * (8-len(Secret)%8) 的代码.

Secret = base64.b32encode(s=Secret.encode('utf-8'))
K = base64.b32decode(Secret, True)

# setup 2 : get current timestamp
# int(time.time()) // 30  到当前经历了多少个30秒
C = struct.pack(">Q", int(time.time()) // 30)  # 将间隔时间转为big-endian(大端序)并且为长整型的字节

# setup 3 : start hmac-sha1
# hmac = SHA1(secret + SHA1(secret + input))
H = hmac.new(K, C,
             hashlib.sha1).digest()  # 使用hmac sha1加密,并且以字节的方式取出 = b'\x0f\x1a\xaeL\x0c\x8e\x19g\x8dv}\xde7\xbc\x95\xeal\xa3\xc1\xee'
O = H[19] & 15  # bin(15)=00001111=0b1111

DynamicPasswd = str((struct.unpack(">I", H[O:O + 4])[0] & 0x7fffffff) % 1000000)
# struct.unpack('>I',h[o:o+4])[0]   -- 转为big-endian(大端序)并且不为负数的数字(整数),因为转换完是一个数组,类似"(2828101188,)",所以需要[0]取出
# h[o:o+4]  --  取其中4个字节  o=10  则取索引分别为 10,11,12,13的字节
# & 0x7fffffff = 11111111  --  与字节转换的数字做与运算
# % 1000000  --  得出的数字与1000000相除然后取余


TOTP = str(0) + str(DynamicPasswd) if len(DynamicPasswd) < 6 else DynamicPasswd
# passwd = passwd if len(passwd) < 6 else str(0) + str(passwd)
# 如果最后得出的6位数字，首位0,可能会只输出5位数字,所以这里进行一个判断，如果是5位则加上首位的0
print(TOTP)

a = 1686038037
b = a // 30

# 1686038039 // 30  # 56201267
# 1686038040 // 30  # 56201268
# 1686038069 // 30  # 56201268
dq = int(time.time()) // 30
dq = 1686038039 // 30
xg = dq + 1
xg * 30

data = [1, 2, 3, 4, 5, 6]
data1 = []
count = 0
for i in data:
    for j in data:
        for k in data:
            if i != j and j != k and i != k:
                data1.append(f'{i}{j}{k}')

print(len(set(data1)))

from itertools import permutations

for i in permutations(data, 3):
    count += 1
print(count)


def my_meta(name, bases, attrs):
    # 修改类的属性和方法
    attrs['custom_attr'] = 123
    attrs['custom_method'] = lambda self: print("Custom method called")

    # 创建修改后的类
    return type(name, bases, attrs)


class MyMeta(metaclass=my_meta):
    # def __new__(cls, name, bases, attrs):
    #     # 修改类的属性和方法
    #     attrs['custom_attr'] = 456
    #     attrs['custom_method'] = lambda self: print("Custom method called")
    #
    #     # 创建修改后的类
    #     return super().__new__(cls, name, bases, attrs)

    pass


class MyClass(MyMeta):
    pass


my_object = MyClass()
print(my_object.custom_attr)  # 输出: 123
my_object.custom_method()  # 输出: Custom method called
