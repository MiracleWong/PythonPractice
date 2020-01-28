#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：回文数
# 地址：http: //www.runoob.com/python/python-exercise-example30.html

# 知识点：回文数知识
# 地址：https://www.cnblogs.com/20175317zrw/p/10923636.html
# Notes: VS Code 的调试Debug文章

a = int(input("请输入一个数字: \n"))
x = str(a)  # 转换为字符串
flag = True

for i in range(int(len(x) / 2)):
    if x[i] != x[-i - 1]:
        flag = False
        break

if flag:
    print("%d 是一个回文数!" % a)
else:
    print("%d 不是一个回文数!" % a)


# // TODO raw_input() 和 input() 的区别
# // TODO VS Code 的调试Debug文章
