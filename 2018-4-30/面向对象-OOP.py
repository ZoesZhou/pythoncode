#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 下午 09:48
# @Author  : Zoe
# @Site    : 
# @File    : 面向对象-OOP.py
# @Software: PyCharm
import abc

# class Person():
#     name = 'NoName'
#     age = 18
#     __score = 0
#     _petname = 'sec'
#
#     def sleep(self):
#         print('Sleeping.......')
#
#
# class Teacher(Person):
#     teacher_id = '3445'
#
#     def make_test(self):
#         print('attention')
#
#
# t = Teacher()
# print(t.name)
# print(t._petname)
# t.sleep()
# print(t.teacher_id)
# t.make_test()


# class Person():
#     name = 'NoName'
#     age = 18
#     __score = 0
#     _petname = 'sec'
#
#     def sleep(self):
#         print('Sleeping.......')
#
#     def work(self):
#         print('make some money')
#
#
# class Teacher(Person):
#     teacher_id = '3445'
#     name = 'Zoe'
#
#     def make_test(self):
#         print('attention')
#
#     def work(self):
#         Person.work(self)  # 扩充父类的功能只需要调用父类相应的相应的函数
#         # 扩充父类的另一种方法，super代表得到父类
#         super().work()
#         self.make_test()
#
#
# t = Teacher()
# t.work()


# class Dog():
#     def __init__(self):
#         print('I am init in dog')
#
#
# d = Dog()


# class Animal(object):
#     def __init__(self):
#         print('Animal')
#
#
# class Reptile(Animal):
#     def __init__(self, name):
#         print('Reptile {0}'.format(name))
#
#
# class Dog(Reptile):
#     def __init__(self):
#         print('Dog')
#
#
# d = Dog()
#
#
# class Cat(Reptile):
#     pass
#
#
# c = Cat(name='kaka')


# class Person(object):
#     name = 'Zoe'
#     age = 18
#
#
# # Mixin设计模式
# class TeacherMixin():
#     def work(self):
#         print('work')
#
#
# class StudentMixin():
#     def study(self):
#         print('study')
#
#
# class TutorMixin(Person, TeacherMixin, StudentMixin):
#     pass
#
#
# tt = TutorMixin()
# print(TutorMixin.__mro__)
# print(tt.__dict__)
# print(TutorMixin.__dict__)

#
# class A():
#     pass
#
#
# class B(A):
#     pass
#
#
# class C():
#     pass
#
#
# print(issubclass(B, A))
# print(issubclass(C, A))
# print(issubclass(B, object))


# class A():
#     name = 'NoName'
#
#
# a = A()
# print(isinstance(a, A))
# print(isinstance(A, A))


# class A():
#     name = 'NoName'
#
#
# a = A()
# print(hasattr(a, 'name'))
# print(hasattr(a, 'age'))


# class A():
#     pass
#
#
# a = A()
# dir(a)


# class Person(object):
#     def fget(self):
#         return self._name * 2
#
#     def fset(self, name):
#         self._name = name.title()
#
#     def fdel(self):
#         self._name = 'NoName'
#
#     name = property(fget, fset, fdel, '对name进行操作')
#
#
# p1 = Person()
# p1.name = 'Zoe Zhou'
# print(p1.name)

# 在用户输入年龄时，可以输入整数，小数，浮点数
# 但内部为了数据清洁，我们统一需要保存整数，直接舍去小数点
# import math
#
#
# class Person(object):
#     def fget(self):
#         return self._age
#
#     def fset(self, age):
#         self._age = math.floor(age)
#
#     def fdel(self):
#         self._age = 'None'
#
#     age = property(fget, fset, fdel, "对age进行操作")
#
#
# p1 = Person()
# p1.age = 18.9
# print(p1.age)


# # __call__举例
# class A(object):
#     def __init__(self, name='NoName'):
#         print("我被调用了")
#
#     def __call__(self):
#         print("我被调用了again")
#
#
# a = A()
# a()


# # __str__举例
# class A(object):
#     def __init__(self, name='NoName'):
#         print("我被调用了")
#
#     def __call__(self):
#         print("我被调用了again")
#
#     def __str__(self):
#         return '嗯..........'
#
#
# a = A()
# print(a)


# # __getattr__举例
# class A(object):
#     name = 'NoName'
#     age = 18
#
#     def __getattr__(self, name):
#         print("没找到")
#         print(name)
#
#
# a = A()
# print(a.name)
# print(a.addr)


# __setattr__案例
# class Person(object):
#     def __init__(self):
#         pass
#
#     def __setattr__(self, name, value):
#         print("设置属性：{0}".format(name))
#         # 下面语句会导致死循环
#         # self.name = value
#         # 此种情况，为了避免死循环，规定统一调用父类魔法函数
#         super().__setattr__(name, value)
#
#
# p = Person()
# print(p.__dict__)
# p.age = 18


# __gt__
# class Student(object):
#     def __init__(self, name):
#         self._name = name
#
#     def __gt__(self, obj):
#         print("哈哈, {0} 会比 {1} 大吗？".format(self, obj))
#         return self._name > obj._name
#
#
# stu1 = Student("one")
# stu2 = Student("two")
# print(stu1 > stu2)

# 抽象类的实现

# 声明一个类并且指定当前类的元类
# class Human(metaclass=abc.ABCMeta):
#     # 定义一个抽象的方法
#     @abc.abstractmethod
#     def smoking(self):
#         pass
#
#     # 定义类抽象方法
#     @classmethod
#     def drink():
#         pass
#
#     @staticmethod
#     def play():
#         pass
#
#     def sleep(self):
#         print('Sleeping.........')


# 利用type造一个类
# 先定义类应该具有的成员函数
def say(self):
    print('Saying......')


def talk(self):
    print('Talking.......')


A = type('AName', (object, ), {'class_say': say, 'class_talk': talk})


a = A()
print(dir(a))
print(a.class_say())
print(a.class_talk())

