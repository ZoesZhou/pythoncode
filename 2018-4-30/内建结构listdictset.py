#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 下午 03:22
# @Author  : Zoe
# @Site    : 
# @File    : 内建结构listdictset.py
# @Software: PyCharm


# def hano(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#         return
#     if n == 2:
#         print(a, '-->', b)
#         print(a, '-->', c)
#         print(b, '-->', c)
#         return
#
#     hano(n-1, a, c, b)
#     hano(1, a, '-->', c)
#     hano(n-1, b, a, c)
#
#
# hano(3, 'A', 'B', 'C')
# i = 0
#
#
# def move(n, a, b, c):
#     global i
#     if n == 1:
#         i += 1
#         print("第", i, "次移动:", a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         move(1, a, '-->', c)
#         move(n-1, b, a, c)
#
#
# move(3, 'A', 'B', 'C')
#
#
# def fib(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     return fib(n-1)+fib(n-2)
#
#
# print(fib(5))


# a = [1, 2, 3, 4, 5]
# length = len(a)
# # indx表示的是list的下标
# indx = 0
# while indx < length:
#     print(a[indx])
#     indx += 1
#


# a = [['one', 1], ['two', 2], ['three', 3]]
# for k, v in a:
#     print(k, '-->', v)


# a = ['a', 'b', 'c']
# b = [i for i in a]
# print(b)
# a = [1, 2, 3, 4, 5]
# b = [i * 10 for i in a]
# print(b)


# 列表生成式可以嵌套
# a = [i for i in range(1, 4)]
# print(a)
# b = [i for i in range(100, 400) if i % 100 == 0]
# print(b)
# c = [m + n for m in a for n in b]
# print(c)
#
# for m in a:
#     for n in b:
#         print(m + n, end=' ')
# print()
# c = [m + n for m in a for n in b if m + n < 250]
# print(c)


a = [x for x in range(1, 100)]
print(len(a))
print(max(a))

b = ['man', 'film', 'python']
print(max(b))

a = 'I love python'
print(list(a))
print(list(range(1, 12)))
