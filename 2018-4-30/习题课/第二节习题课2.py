#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 下午 08:42
# @Author  : Zoe
# @Site    : 
# @File    : 第二节习题课2.py
# @Software: PyCharm

'''
while True:

    # 实心矩形
    def s_jx():
        # 控制行
        for i in range(1, 5):
            # 控制列
            for j in range(1, 6):
                print('*', end=' ')
            # 当第i行的5列输出完后进行换行
            print()


    # 打印空心矩形
    def o_jx():
        for i in range(1, 5):
            for j in range(1, 5):
                if i == 1 or i == 4 or j == 1 or j == 4:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()


    # 打印正直角三角形
    def u_sj():
        for i in range(1, 6):
            for j in range(6-i, 6):
                print('*', end=' ')
            print()


    # 打印正直角空心三角形
    def v_sj():
        for i in range(1, 6):
            for j in range(6-i, 6):
                if i == 1 or i == 5 or j == 6-i or j == 5:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()

    print("输入0结束")
    shape = input("请输入实心矩形或实心正三角形或空心矩形或空心正三角形:")
    if shape == '0':
        break
    elif shape == "实心矩形":
        s_jx()
    elif shape == "实心正三角形":
        u_sj()
    elif shape == "空心矩形":
        o_jx()
    elif shape == "空心正三角形":
        v_sj()
    else:
        print("是不是撒")

'''

# 打印字母D
# for i in range(1, 5):
#     for j in range(1, 4):
#         if j == 1:
#             print('*', end=' ')
#         elif i == 1 or i == 4:
#             if j > 2:
#                 break
#             print('*', end=' ')
#         elif j == 3:
#             if i == 2 or i == 3:
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# 打印字母B
# for i in range(1, 4):
#     for j in range(1, 4):
#         if j == 1:
#             print('*', end=' ')
#         elif i == 1 or i == 4:
#             if j > 2:
#                 break
#             else:
#                 print('*', end=' ')
#         elif j == 3:
#             if i == 2 or i == 3:
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
#
# for i in range(1, 5):
#     for j in range(1, 4):
#         if j == 1:
#             print('*', end=' ')
#         elif i == 1 or i == 4:
#             if j > 2:
#                 break
#             else:
#                 print('*', end=' ')
#         elif j == 3:
#             if i == 2 or i == 3:
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# 打印字母R
for i in range(1, 6):
    for j in range(1, 4):
        if j == 1:
            print('*', end=' ')
        elif j == 2:
            if i == 2 or i == 3 or i == 5:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        elif j == 3:
            if i == 2 or i == 3 or i == 5:
                print('*', end=' ')
            else:
                print(' ', end=' ')

    print()


