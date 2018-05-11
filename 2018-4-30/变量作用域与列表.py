#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 上午 09:01
# @Author  : Zoe
# @Site    : 
# @File    : 变量作用域与列表.py
# @Software: PyCharm
# a1 = 100
#
#
# def fun():
#     print(a1)
#     print("I am is fun")
#     a2 = 99
#     print(a2)
#
#
# print(a1)
# fun()
# print(a2)

# b1 = 100
#
#
# def fun():
#     global b1
#     b1 = 1
#     print(b1)
#     print('I am is fun')
#     b2 = 99
#     print(b2)
#
#
# print(b1)
# fun()


# a = 1
# b = 2
#
#
# # globals和locals叫内建函数
# def fun(c, d):
#     e = 111
#     print("Locals={0}".format(locals()))
#     print("Globals={0}".format(globals()))
#
#
# fun(100, 200)


# x = 100
# y = 200
# z1 = x + y
# z2 = eval('x + y')
# print(z1)
# print(z2)
# print('*'*20)
# z3 = exec('x + y')
# z4 = exec("print('x+y:', x + y)")
# print(z3)
# print(z4)


# x = 0
#
#
# def fun():
#     global x
#     x += 1
#     print(x)
#     fun()
#
#
# fun()


# def fib(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
#
# print(fib(10))

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(L[-2:-4])
print(L[-2:-4:-1])

print('#'*20)
L1 = L[:]
L2 = L
print(id(L))
print(id(L1))
print(id(L2))

