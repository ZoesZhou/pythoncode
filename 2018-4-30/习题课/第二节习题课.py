#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/1 下午 05:15
# @Author  : Zoe
# @Site    : 
# @File    : 第二节习题课.py
# @Software: PyCharm

# 打印矩形
# for i in range(1, 5):
#     for j in range(1, 5):
#         print('*', end=' ')
#     print()


# 打印空心矩形
# for i in range(1, 5):
#     for j in range(1, 5):
#         if i == 1 or i == 4 or j == 1 or j == 4:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
#

# 打印正直角三角形
# for i in range(1, 6):
#     for j in range(6-i, 6):
#         print('*', end=' ')
#     print()
# print('='*20)
#
# for i in range(1, 6):
#     for j in range(6-i, 6):
#         if i == 1 or i == 5 or j == 6-i or j == 5:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# print('='*20)

# 打印直角三角形
# for i in range(1, 6):
#     for j in range(1, 7-i):
#         print('*', end=' ')
#     print()
# print('='*20)
#
# 打印直角空心三角形
# for i in range(1, 6):
#     for j in range(1, 7-i):
#         if i == 1 or i == 5 or j == 1 or j == 6-i:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# print('='*20)

# 打印等腰三角形
# for i in range(1, 6):
#     # 更改打印起始位置,一个*号是两个空格
#     for k in range(1, 7-i):
#         print(end=' ')
#     # 控制列,规则是第一行一列,第二行是二列
#     for j in range(6-i, 6):
#         print('*', end=' ')
#     print()
# print('='*20)

# 打印空心等腰三角形
# for i in range(1, 6):
#     for k in range(1, 6-i):
#         print(end=' ')
#     for j in range(6-i, 6):
#         if i == 1 or i == 5 or j == 6-i or j == 5:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# print('='*20)
# 打印字母A
# for i in range(1, 6):
#     for k in range(1, 6-i):
#         print(end=' ')
#     for j in range(6-i, 6):
#         if i == 1 or i == 3 or j == 6-i or j == 5:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# print('='*20)
# 打印菱形
# for i in range(1, 5):
#     for k in range(1, 7-i):
#         print(end=' ')
#     for j in range(6-i, 6):
#         print('*', end=' ')
#     print()
# for i in range(1, 6):
#     for k in range(i):
#         print(end=' ')
#     for j in range(6-i):
#         print('*', end=' ')
#     print()
# print('='*20)
# 打印空心菱形
# for i in range(1, 5):
#     for k in range(1, 7-i):
#         print(end=' ')
#     for j in range(6-i, 6):
#         if i == 1 or j == 6-i or j == 5:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# for i in range(1, 6):
#     for k in range(i):
#         print(end=' ')
#     for j in range(6-i):
#         if i == 5 or j == 0 or j == 6-i-1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# print('='*20)

# 打印梯形
# for i in range(1, 6):
#     for k in range(1, 6-i):
#         print(end=' ')
#     for j in range(6-i, 9):
#         print('*', end=' ')
#     print()
# print('='*20)

# 打印空心梯形
# for i in range(1, 6):
#     for k in range(1, 6-i):
#         print(end=' ')
#     for j in range(6-i, 9):
#         if i == 1 or i == 5 or j == 6-i or j == 8:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# print('='*20)

# 打印字母D
# for m in range(4):
#     for n in range(3):
#         if n == 0:
#             print('*', end=' ')
#         elif m == 0 or m == 3:
#             if n == 2:
#                 break
#             else:
#                 print('*', end=' ')
#         elif n == 2:
#             if m == 0 or m == 3:
#                 break
#             else:
#                 print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print('')
# print('='*20)

# 打印字母R
# for m in range(5):
#     for n in range(4):
#         if n == 0:
#             print('*', end=' ')
#         elif m == 0 or m == 3:
#             if n == 2:
#                 break
#             else:
#                 print('*', end=' ')
#         elif n == 2:
#             if m == 0 or m == 3:
#                 break
#             else:
#                 print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print('')
# print('='*20)

# 打印字母B
# for m in range(3):
#     for n in range(3):
#         if n == 0:
#             print('*', end=' ')
#         elif m == 0 or m == 3:
#             if n == 2:
#                 break
#             else:
#                 print('*', end=' ')
#         elif n == 2:
#             if m == 0 or m == 3:
#                 break
#             else:
#                 print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print('')
# for m in range(4):
#     for n in range(3):
#         if n == 0:
#             print('*', end=' ')
#         elif m == 0 or m == 3:
#             if n == 2:
#                 break
#             else:
#                 print('*', end=' ')
#         elif n == 2:
#             if m == 0 or m == 3:
#                 break
#             else:
#                 print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print('')



