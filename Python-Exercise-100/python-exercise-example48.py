#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example48.html


def compare(a, b):
    maxSum = max(a, b)
    minSum = min(a, b)
    print("%s比%s大" % (maxSum, minSum))


if __name__ == "__main__":
    a = 10
    b = 20
    compare(a, b)

