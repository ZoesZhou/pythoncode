#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 下午 08:33
# @Author  : Zoe
# @Site    : 
# @File    : 内建结构3.py
# @Software: PyCharm

# count：计算制定数据出现的次数
# index：求制定元素在元组中的索引位置
# 如果需要查找的数字是多个，则返回第一个
# t = (2, 1, 2, 3, 45, 1, 1, 2)
# print(t.count(2))
# print(t.index(45))
# print(t.index(1))


# 变量交换
# a = 1
# b = 3
# a, b = b, a
# print(a)
# print(b)

# s = set()
# print(type(s))
# a = {1, 2, 3, 4, 5}
# print(type(a))
# d = {}
# print(type(d))

# 集合内涵
# s = {23, 23, 1, 2, 3, 4, 3, 2, 1, 2233, 345}
# print(s)
#
# ss = {i for i in s}
# print(ss)
#
# sss = {i for i in s if i % 2 == 0}
# print(sss)
#
# s1 = {1, 2, 3, 4}
# s2 = {'i', 'love', 'python'}
# s = {m*n for m in s2 for n in s1}
# print(s)
#
# s = {m*n for m in s2 for n in s1 if n == 2}
# print(s)

# 集合函数
# l = [1, 2, 3, 4, 34, 1, 2, 3, 4]
# s = set(l)
# print(s)
#
# s = {1}
# s.add(343)
# print(s)
#
# s = {1, 2, 3, 4, 5}
# print(id(s))
# s.clear()
# print(id(s))


# s = {23, 3, 4, 5, 1, 2, 3}
# s.remove(4)
# print(s)
# s.discard(1)
# print(s)
#
# print('#'*20)
#
# s.discard(1100)
# print(s)
#
# s.remove(2200)
# print(s)

# pop随机一处一个数
# s = {1, 2, 3, 4, 5}
# d = s.pop()
# print(d)
# print(s)


# s1 = {1, 2, 3, 4, 5, 6}
# s2 = {5, 6, 7, 8, 9}
#
# s_1 = s1.intersection(s2)
# print(s_1)
#
# s_2 = s1.difference(s2)
# print(s_2)
#
# s_3 = s1.issubset(s2)
# print(s_3)


# s1 = {1, 2, 3, 4, 5, 6}
# s2 = {5, 6, 7, 8, 9}
# s_1 = s1 - s2
# print(s_1)
# s_2 = s1 + s2
# print(s_2)


# s = frozenset()
# print(type(s))
# print(s)


# d = {'one': 1, 'two': 2, 'three': 3}
# print(d['one'])
#
# d['one'] = 'eins'
# print(d)
#
# del d['one']
# print(d)

# d = {'one': 1, 'two': 2, 'three': 3}
# if 'two' in d:
#     print('key')


# d = {'one': 1, 'two': 2, 'three': 3}
#
# for k in d:
#     print(k, d[k])
#
# # 上述代码可以改写成如下
# print('%'*20)
# for k in d.keys():
#     print(k, d[k])
#
# print('&'*20)
# # 只访问字典的值
# for v in d.values():
#     print(v)
#
# print('^'*20)
# for k, v in d.items():
#     print(k, '--', v)

# d = {'one': 1, 'two': 2, 'three': 3}
#
# # 加限制条件的字典生成式
# dd = {k: v for k, v in d.items() if v % 2 == 0}
# print(dd)


# d = {'one': 1, 'two': 2, 'three': 3}
# print(str(d))


# d = {'one': 1, 'two': 2, 'three': 3}
# i = d.items()
# print(type(i))
# print(i)

#
# d = {'one': 1, 'two': 2, 'three': 3}
#
# # keys:返回字典的键组成的一个结构
# k = d.keys()
# print(type(k))
# print(k)
# print('%'*20)
# # values:返回字典的值组成的一个可迭代的结构
# v = d.values()
# print(type(v))
# print(v)

# d = {'one': 1, 'two': 2, 'three': 3}
# print(d.get('on33'))
#
# # get默认值是 None ，可以设置
# print(d.get('one', 100))
# print(d.get('one33', 100))
#
# # 体会以下代码和上面代码的区别
# print(d['on33'])


L = ['eins', 'zwei', 'drei']
# 注意fromkeys两个参数的类型
# 注意fromkeys的调用主体
d = dict.fromkeys(L, 'hello')
print(d)
