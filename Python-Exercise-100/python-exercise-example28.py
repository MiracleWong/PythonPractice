#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http://www.runoob.com/python/python-exercise-example28.html


def age(n):
    if n == 1:
        c = 10
    else:
        c = age(n - 1) + 2
    return c


print(age(5))
