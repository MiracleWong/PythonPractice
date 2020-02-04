#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：变量值交换
# 地址：http: //www.runoob.com/python/python-exercise-example47.html


def exchange(a, b):
    a, b = b, a
    return (a, b)


if __name__ == "__main__":
    x = 10
    y = 20
    print("x = %d,y = %d" % (x, y))
    x, y = exchange(x, y)
    print("x = %d,y = %d" % (x, y))

