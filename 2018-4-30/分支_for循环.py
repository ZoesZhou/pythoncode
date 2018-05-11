#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/30 上午 10:11
# @Author  : Zoe
# @Site    : 
# @File    : 分支_for循环.py
# @Software: PyCharm
# score = input('请输入学生成绩：')
# score = int(score)
#
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('起开，我没你这撒学僧')


# for i in range(1, 11):
#     if i == 7:
#         print('我找到了')
#         break
#     else:
#         print(i)


for i in range(1, 11):
    if i % 2 == 1:
        continue

    print('{} 是偶数'.format(i))

print()

for i in range(1, 11):
    if i % 2 == 0:
        print('{} 是偶数'.format(i))

print()

for i in range(1, 11):
    if i % 2 == 1:
        continue
    else:
        print('{}是偶数'.format(i))

