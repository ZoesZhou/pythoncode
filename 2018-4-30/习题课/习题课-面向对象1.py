#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 下午 08:16
# @Author  : Zoe
# @Site    : 
# @File    : 习题课-面向对象1.py
# @Software: PyCharm


# 打印字母a
def a():
    for i in range(1, 6):
        for k in range(6-i):
            print('', end=' ')
        for j in range(1, i+1):
            if i == 1 or i == 4 or j == 1 or j == i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()


# 打印字母b
def b():
    for i in range(1, 4):
        for j in range(1, 4):
            if i == 1 or i == 4 or j == 1:
                if j < 3:
                    print('*', end=' ')
            elif j == 3:
                if i == 2 or i == 3:
                    print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

    for i in range(1, 5):
        for j in range(1, 4):
            if i == 1 or i == 4 or j == 1:
                if j < 3:
                    print('*', end=' ')
            elif j == 3:
                if i == 2 or i == 3:
                    print('*', end=' ')
            else:
                print(' ', end=' ')
        print()


# 打印字母c
def c():
    for i in range(1, 5):
        for j in range(1, 4):
            if i == 1 or i == 4:
                if j > 1:
                    print('*', end=' ')
            elif j == 3:
                if i == 2 or i == 3:
                    print('*', end=' ')
            else:
                print(' ', end=' ')
        print()


# 打印字母d
def d():
    for i in range(1, 5):
        for j in range(1, 4):
            if i == 1 or i == 4 or j == 1:
                if j < 3:
                    print('*', end=' ')
            elif j == 3:
                if i == 2 or i == 3:
                    print('*', end=' ')
            else:
                print(' ', end=' ')
        print()





