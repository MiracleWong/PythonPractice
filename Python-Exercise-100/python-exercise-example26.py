#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：递归
# 地址：http: //www.runoob.com/python/python-exercise-example26.html


def factorial(n):
    sum = 0
    if n == 0:
        sum = 1
    else:
        sum = n * factorial(n - 1)
    return sum


if __name__ == "__main__":
    print("阶乘结果为：{}".format(factorial(5)))
