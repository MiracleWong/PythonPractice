#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http://www.runoob.com/python/python-exercise-example19.html

from sys import stdout

# for n in range(2, 1001):
#     print(n)


def perfectNumber(num):
    sum = 1
    for n in range(2, num):
        if num % n == 0:
            sum += n
    if sum == num:
        return num


if __name__ == "__main__":
    for n in range(2, 1001):
        if perfectNumber(n) != None:
            print(perfectNumber(n))
    # print(perfectNumber(6))

# for i in range(1, 1001):
#     sum = 0
#     for j in range(1, i):
#         if i % j == 0:
#             sum += j
#     if sum == i:
#         print(i)
