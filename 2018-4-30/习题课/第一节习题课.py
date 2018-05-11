#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/30 下午 09:37
# @Author  : Zoe
# @Site    : 
# @File    : 第一节习题课.py
# @Software: PyCharm
# str1 = "我的身高是 {0}, 体重是 {1}"
# res = str1.format('175cm', '66kg')
# print(res)
#
# str2 = "我的身高是 {height}, 体重是 {weight}"
# res = str2.format(height='175cm', weight='66kg')
# print(res)

# str1 = "我的身高是 {0[0]}, 体重是{0[1]}"
# res = str1.format(['175cm', '66kg'])
# print(res)
#
# str1 = "我的身高是 {0[h]}, 体重是{0[w]}"
# dict1 = {'h': '175cm', 'w': '66kg'}
# res = str1.format(dict1)
# print(res)

# res = '我知道pi的值是 {:0.3f}'.format(3.1415926)
# print(res)
#
# res = '10的二进制是 {:b}'.format(10)
# print(res)
# res = '10的八进制是 {:o}'.format(10)
# print(res)
# res = '10的十六进制是 {:x}'.format(10)
# print(res)
# res = '10的十进制是 {:d}'.format(10)
# print(res)

# print(10000000000000000)
# res = '我值 {:,}多钱'.format(9000000000000000000)
# print(res)

# res = 'ilovepython {:>8}'.format(123)
# print(res)
# res = 'ilovepython {:*>8}'.format(123)
# print(res)
# res = 'ilovepython {:*<8}'.format(123)
# print(res)
# res = 'ilovepython {:*^8}'.format(123)
# print(res)


# row = input("请输入行数：")
# rank = input("请输入列数：")
# row = int(row)
# rank = int(rank)
#
# # 这个循环控制行
# for i in range(row):
#     # 这个循环控制列
#     for j in range(rank):
#         print('*', end=' ')
#     print('')

# for i in range(5):
#     for j in range(5-i):
#         print(j, end=' ')
#     print()

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%dx%d=%-2d ' % (i, j, i*j), end=' ')
#     print()


# rows = input('请输入列数：')
#
# for i in range(0, rows+1):
#     for j in range(0, rows-i):
#         print()


