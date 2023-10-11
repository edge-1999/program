class SessionStorage(object):
    def __iter__(self):
        return iter(['a', 'b', 'c', 'd'])


# obj = SessionStorage()
# for it in obj:
#     print(it)


# 自定义迭代器类，迭代打印字符串中的每个字符
class StringIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        char = self.string[self.index]
        self.index += 1
        return char


#
# # 使用迭代器迭代打印字符串中的每个字符
# string = "Hello, World!"
# iterator = StringIterator(string)
# co = 0
# for char in iterator:
#     if co > 2:
#         break
#     else:
#         print(char)
#     co += 1


# for char in iterator:
#     print('asdfv', char)


class CounterIterator:
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter >= 5:
            raise StopIteration
        return self.counter


# class SessionStorage(object):
#     def __iter__(self):
#         return CounterIterator()
#
#
# obj = SessionStorage()
# for it in obj:
#     print(it)


class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


class XRange(object):
    def __init__(self, st, en):
        self.st = st
        self.en = en

    def __iter__(self):
        return MyRange(self.st, self.en)


# 使用示例
my_range = XRange(0, 3)

for i in my_range:
    print(i)

from collections.abc import Iterator, Iterable

v1 = [11, 22, 33, 44]
print(isinstance(v1, Iterable))  # 判断对象是否可迭代 判断是否有__iter__，且返回可迭代对象
print(isinstance(v1, Iterator))  # 判断对象是否是迭代器 判断是否有__iter__、__next__
