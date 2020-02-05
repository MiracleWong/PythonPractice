#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：移位操作取数字
# 地址：http: //www.runoob.com/python/python-exercise-example54.html

# 知识点：
# 地址：
# Notes:

if __name__ == "__main__":
    # a = int(raw_input('input a number:\n'))
    a = 9
    b = a >> 4
    print(b)
    c = ~(~0 << 4)
    print(c)
    d = b & c
    print("八进制显示数字为：%o\t%o" % (a, d))

