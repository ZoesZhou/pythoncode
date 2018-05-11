#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 下午 09:47
# @Author  : Zoe
# @Site    : 
# @File    : 函数到结束.py
# @Software: PyCharm


# args 把他看作一个list
# def stu(*args):
#     print("Hello 大家好，我自我介绍一下，简单说说两句：")
#     print(type(args))
#     for item in args:
#         print(item)
#
#
# stu("Zoe", 18, "江西省吉安市", "single")
# stu("周永生")

# def stu(**kwargs):
#     # 在函数体内对于kwargs的使用不用带星号
#     print("Hello 大家好，我先自我介绍一下：")
#     print(type(kwargs))
#     for k, v in kwargs.items():
#         print(k, '---', v)
#
#
# stu(name='Zoe', age=18, addr="江西省吉安市", lover='python', work='programmer')
# print('*'*20)
# stu(name="周永生")

# def stu(*args):
#     print("hahahah")
#     n = 0
#     for i in args:
#         print(type(i))
#         print(n)
#         n += 1
#         print(i)
#
#
# L = ["Zoe", 18, "周永生"]
# stu(*L)

# def stu(name, age):
#     """
#     这是文档的内容
#     :param name:表示学生的姓名
#     :param age:表示学生的年龄
#     :return:此函数没有返回值
#     """
#     pass
#
#
# print(help(stu))
# print('*'*20)
# print(stu.__doc__)


def stu(name, age, *args, hobby="没有", **kwargs):
    print("Hello 大家好")
    print("我叫{0}, 我今年{1}岁。".format(name, age))
    if hobby == "没有":
        print("我没有爱好，I'm sorry")
    else:
        print("我的爱好是{0}".format(hobby))

    print('*'*20)

    for i in args:
        print(i)

    print('#'*20)

    for k, v in kwargs.items():
        print(k, '---', v)


name = 'Zoe'
age = 18
stu(name, age)
stu(name, age, hobby='游泳')
stu(name, age, 'rtg', '533', hobby='游泳', hobby1='烹饪')



