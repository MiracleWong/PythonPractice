#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：阶乘求和
# 地址：http: //www.runoob.com/python/python-exercise-example25.html

# 知识点：阶乘和reduce


# Tn = 0
# t = 1
# for n in range(1, 21):
#     t *= n
#     Tn += t
# print("阶乘求和为： {}".format(Tn))

from functools import reduce

a = 0
for n in range(1, 21):
    a += reduce(lambda x, y: x * y, range(1, n + 1))
print("阶乘求和为： {}".format(a))
