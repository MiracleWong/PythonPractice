#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example89.html
from sys import stdout

if __name__ == "__main__":
    # a = int(input("输入四个数字:\n"))
    a = 1234
    aa = []
    aa.append(int(a % 10))
    aa.append(int(a % 100 / 10))
    aa.append(int(a % 1000 / 100))
    aa.append(int(a / 1000))

    for i in range(4):
        aa[i] += 5
        aa[i] %= 10
    for i in range(2):
        aa[i], aa[3 - i] = aa[3 - i], aa[i]
    for i in range(3, -1, -1):
        stdout.write(str(aa[i]))
