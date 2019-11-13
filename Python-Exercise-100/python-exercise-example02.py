#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http://www.runoob.com/python/python-exercise-example2.html

zname
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]


def net_profits():
    i = int(input("净利润："))
    r = 0
    for index in range(0, 6):
        if i > arr[index]:
            r += (i - arr[index]) * rat[index]
            i = arr[index]
    return r


if __name__ == "__main__":
    print(net_profits())
