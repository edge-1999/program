lst = []

from collections import Counter

l = ['fa|aaaa|fsjkedf|\n', 'sdaffs|asdffdsa|0|0|||a1|a1|a1|\n']
for i in l:
    lst.extend(i.strip('\n').split('|'))
    # print(ls)
d2 = Counter(lst)
# print(d2.items())
sorted_x = sorted(d2.items(), key=lambda x: x[1], reverse=True)  # key：按照元组的第二个元素排序；reverse：升降排序
print(sorted_x)
data = [1, 1, 2, 3, 78, 5, 3, 6, 8, 3, 3, 0, 0, 7, 4, 5, 7, ]

# data_s = sorted(data, key=, reverse=True)

dic = sorted(d2.items(), key=lambda x: x[0], reverse=True)


class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()
print(hasattr(point1, 'x'))
print(hasattr(point1, 'y'))
print(hasattr(point1, 'z'))
print(hasattr(point1, 'no'))  # 没有该属性


# 类(class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 实例化：创建一个类的实例，类的具体对象。
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。 方法：类中定义的函数。
# 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
# 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样 一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a） "关系（例图，Dog是一个Animal）。
# 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
# class Baoan13(object):  # 新式类 定义一个类，并且继承object类，父类、基类、超类
# class BaoAn13:  # 经典类，参数列表中没有object
#     head = '我是一个类变量'  # 类变量，可以被类中所有的实例方法调用，不作为实例变量使用
#
#     def __init__(self, name, age, hig):  # 构造方法，又称构造函数。作用：初始化类的属性
#         # 定义：在类里面，双下滑线构成私有方法，只能被自身或子类访问
#         self.name = name  # 实例变量（用self修饰的一个变量）
#         self.age = age
#         self.hig = hig
#
#     def play(self):  # 实例方法（实例函数）
#         print(self.name + '今年' + self.age + '岁了，他的身高是' + self.hig + 'cm。')
#
#     def get_play(self):  # 这个实例方法是调用上面play的实例方法
#         self.play()
#
#     @classmethod  # @classmethod是一个类方法的装饰器
#     # 在类中，@开头的称为装饰器
#     # 装饰器的作用：本身也是一个函数，在不影响原有功能的基础上，添加新的功能
#     def func1(cls):  # 类方法，以cls修饰的一个方法，类方法的特性：单例模式
#         print('我是一个类方法。')
#
#     def func2(cls):  # 这也是一个类方法，与上面有@classmethod修饰的不一样
#         cls.value = 20  # 类方法变量
#         print(cls.value)
#
#     @staticmethod  # 静态方法的装饰器
#     # 静态方法：写在类中的普通方法，能被实例方法和类方法调用，但是不能调用实例方法和类方法
#     def func():
#         print('我是一个任人调用的静态方法。')
#
#     def putong:
#         print('我只是一个普通函数。')


class Functor(object):

    def __init__(self, context):
        self._context = context

    def __call__(self):
        print("do something with {}".format(self._context))


lai_functor = Functor("lai")
yong_functor = Functor("yong")
lai_functor()  # 调用对象，执行 __call__() 协议内定义动作
yong_functor()
