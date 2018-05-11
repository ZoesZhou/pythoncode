#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 下午 08:42
# @Author  : Zoe
# @Site    : 
# @File    : 内建结构2.py
# @Software: PyCharm


# def a(n):
#     n[2] = 300
#     print(n)
#     return
#
#
# def b(n):
#     n += 100
#     print(n)
#     return
#
#
# an = [1, 2, 3, 4, 5, 6]
# bn = 9
# print(an)
# a(an)
# print(an)
#
# print(bn)
# b(bn)
# print(bn)


# a = [i for i in range(1, 5)]
# print(a)
# a.append(100)
# print(a)
# a.insert(3, 666)
# print(a)
# i = a.pop()
# print(i)
# print(a)
#
#
# print(id(a))
# a.remove(666)
# print(a)
# print(id(a))
#
# a.reverse()
# print(a)
# print(id(a))
#
#
# b = [7, 8, 9]
# a.extend(b)
# print(a)
# print(id(a))
#
# print('*'*20)
# d = [i for i in range(1, 10)]
# d.append(8)
# d.insert(3, 8)
# print(d)
# d_len = d.count(8)
# print(d_len)
# print('#'*20)
# a = [1, 2, 3, 4, 5, 666]
# print(a)
# # list类型，简单赋值操作，是传地址
# b = a
# b[3] = 777
# b.copy()
# print(a)
# print(b)
# print('&'*20)
#
#
# b = a.copy()
# print(b)
# print(id(a))
# print(id(b))
# print('%'*20)
# b[3] = 888
# print(b)

# 深拷贝和浅拷贝的区别
# 出现以下问题的原因，copy函数是个浅拷贝，即只拷贝一层内容
# 深拷贝需要使用特定工具
# a = [1, 2, 3, [10, 20, 30]]
# b = a.copy()
# print(id(a))
# print(id(b))
# print(id(a[3]))
# print(id(b[3]))
# a[3][2] = 666
# print(a)
# print(b)

# 创建一个只有一个值的元组
# t = (1,)
# m = 1,
# print(t)
# print(m)
# n = (1)
# print(n)


# 单层元组遍历
t = ((1, 2, 3), (2, 3, 4), ('i', 'love', 'python'))
for i in t:
    print(i, end=' ')
print()

# 双层元组遍历
for k, v, m in t:
    print(k, '---', v, '---', m)






