#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/30 上午 09:05
# @Author  : Zoe
# @Site    : 
# @File    : 变量_操作符.py
# @Software: PyCharm
s = '%s using python'
print(s % 'Zoe')

print('I am %d years old' % 18)

a = 'I am %s, I am %d years old'
print(a % ('Zoe', 18))

q = 'Yes, i am {1} years old, I love {0} and {1} years old'.format('python', 18)
print(q)
