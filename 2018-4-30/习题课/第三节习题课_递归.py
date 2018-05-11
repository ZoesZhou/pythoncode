#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 下午 08:09
# @Author  : Zoe
# @Site    : 
# @File    : 第三节习题课_递归.py
# @Software: PyCharm


# 类似于栈的先进后出模式
# 要有递推关系
# 要有临界
# def digui(num):
#     print('$' + str(num))
#     if num > 0:
#         # 这里用的是调用函数本身的函数
#         digui(num-1)
#     else:
#         print('='*20)
#     print(num)
#
#
# digui(3)


i = 0


def move(n, a, b, c):
    global i
    if n == 1:
        i += 1
        print("移动第", i, "次", a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
        print(0)


move(3, 'A', 'B', 'C')





