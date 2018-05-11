#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/30 下午 02:19
# @Author  : Zoe
# @Site    : 
# @File    : while_函数.py
# @Software: PyCharm
principal = 100000
year = 0
while principal < 200000:
    principal = principal * (1 + 0.067)
    year += 1
    print('第 {0} 年拿了 {1} 块钱'.format(year, principal))
else:
    print()
    print('大爷的，终于翻倍了，10多年呀')
