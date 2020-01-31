#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 地址：http: //www.runoob.com/python/python-exercise-example24.html

# 知识点：斐波那契数列

a = 2
b = 1
s = 0
for n in range(1, 21):
    s += a / b
    a, b = a + b, a
print("数列求和为：{}".format(s))

