#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：判断质数
# 地址：http: //www.runoob.com/python/python-exercise-example12.html

# 知识点：Python如何判断一个质数
# 地址：https://www.runoob.com/python/python-get-prime-number.html
# Notes:
# 判断素数的方法：用一个数分别去除以2到sqrt(这个数)（就是这个数的开平方），如果能被整除，则表明此数不是素数，反之是素数。

h = 0
leap = 1
from math import sqrt
from sys import stdout

for m in range(101, 201):
    k = int(sqrt(m + 1))
    for i in range(2, k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print("%-4d" % m)
        h += 1
        if h % 10 == 0:
            print()
    leap = 1

print("The total is %d " % h)
