#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http://www.runoob.com/python/python-exercise-example6.html
def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
        # print(a)
    return a


print(fib(15))
