#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http://www.runoob.com/python/python-exercise-example18.html
from functools import reduce

Tn = 0
Sn = []
n = int(input("n = "))
a = int(input("a = "))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)
Sn = reduce(lambda x, y: x + y, Sn)
print("计算和为：", Sn)

# // TODO reduce 的用处

