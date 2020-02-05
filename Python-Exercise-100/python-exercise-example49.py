#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：lambda函数
# 地址：http: //www.runoob.com/python/python-exercise-example49.html

# 知识点：匿名函数
# 地址：https://www.liaoxuefeng.com/wiki/1016959663602400/1017451447842528


MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
MINIMUM = lambda x, y: (x > y) * y + (x < y) * x

if __name__ == "__main__":
    a = 10
    b = 20
    print("The largar one is %d" % MAXIMUM(a, b))
    print("The lower one is %d" % MINIMUM(a, b))

