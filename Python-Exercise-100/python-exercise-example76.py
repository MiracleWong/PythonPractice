#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：even odd
# 地址：http: //www.runoob.com/python/python-exercise-example76.html


def even(n):
    sum = 0.0
    for i in range(2, n + 1, 2):
        sum += 1.0 / i
    return sum


def odd(n):
    sum = 0.0
    for i in range(1, n + 1, 2):
        sum += 1.0 / i
    return sum


if __name__ == "__main__":
    # num = int(input("请输入一个数字: \n"))
    num = 7
    if num % 2 == 0:
        print(even(num))
    else:
        print(odd(num))

