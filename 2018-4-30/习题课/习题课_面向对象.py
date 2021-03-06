#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 下午 09:57
# @Author  : Zoe
# @Site    : 
# @File    : 习题课_面向对象.py
# @Software: PyCharm
import random
'''
输入一个三位数与程序随机数比较大小
1、如果大于程序随机数，则分别输出这个三位数的个位、十位、百位
2、如果等于程序随机数，则提示中将，记100分
3、如果小于程序随机数，则将120个字符输入到文本中
(规则是每一条字符串的长度为12，单独占一行，并且前四个是字母，后八个是数字)
'''


class GameNum(object):
    def line(self):
        # 定义一个空字符串用于拼接字符
        str_num = ''
        # 循环前四个随即字母（用ascii码对应的值来随机再转换为字母）
        for i in range(4):
            # 随机小写字母的ascii码值
            num = random.randrange(97, 123)
            # 将ascii码值转换成对应的字母
            str_s = chr(num)
            # 依次拼接得到的随即字母
            str_num = str_num + str_s
        # 循环后八个随机数字
        for i in range(8):
            num = random.randrange(0, 10)
            str_num = str_num + str(num)
        return str_num

    def num_game(self, total, source):
        while True:
            num = input("请输入一个三位数,输入-1结束：")
            if num == '-1':
                break
            # 程序随机数
            random_num = random.randrange(100, 1000)
            # 检测输入是否是纯数字
            if num.isdigit() and 100 <= int(num) <= 999:
                # 计算有效输入多少次
                total += 1
                print("输入{}次".format(total))
                num = int(num)
                random_num = int(random_num)
                # 判断随机数与输入数的大小
                if num > random_num:
                    # 求百位数字方法是地板除100或用数学模块中的floor()函数
                    hundreds = num // 100
                    # 求十位数字方法就是把三位数取除100的余数，再地板除10
                    tens = (num % 100) // 10
                    # 求个位数字直接取10的余数
                    units = num % 10
                    print("你输入的数比程序随机数大，程序随机数是", random_num)
                    print("这个三位数的百位数是{0}，十位数是{1}，"
                          "个位数是{2}".format(hundreds, tens, units))

                if num == random_num:
                    # 所得分数
                    source += 100
                    print("你中奖了，目前分数为", source)
                    print("你中奖的概率是多少", source/total)
                if num < random_num:
                    print("你输入的数比程序随机数小，程序随机数是", random_num)
                    # 由于120个字符每行12个只需存入10行就行
                    for i in range(10):
                        str_line = GameNum.line(self)
                        # 执行文件存入操作
                        with open('str_num.txt', 'a') as f:
                            f.write(str_line + '\n')

            else:
                print("请按规定输入：")


# 程序入口
if __name__ == '__main__':  # 调试代码
    # 在本身模块中__name__ == __main__，当第三方导入的时候__name__ == 文件名
    # print(__name__)
    # 定义一个变量用于存取初始分数
    source = 0
    # 定义一个变量用于累计输入多少次
    total = 0
    # num_game(total, source)
    game_num1 = GameNum()
    game_num1.num_game(total, source)

