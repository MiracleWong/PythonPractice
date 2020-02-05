#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：按位取反~
# 地址：http: //www.runoob.com/python/python-exercise-example.html

# 知识点：按位取反~
# 地址：https://www.cnblogs.com/zhgyki/p/9452637.html

if __name__ == "__main__":
    a = 8  # 11101010
    b = ~a  # 00010101
    print("The a's 1 complement is %d" % b)
    a = ~a  #
    print("The a's 2 complement is %d" % a)

