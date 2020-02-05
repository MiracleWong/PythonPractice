#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：异位或
# 地址：http: //www.runoob.com/python/python-exercise-example53.html

# 知识点：异位或
# Notes:
# 0^0=0; 0^1=1; 1^0=1; 1^1=0
if __name__ == "__main__":
    a = 0x77  # 01110111 十进制结果为119
    b = a ^ 3  # 0011
    print("a & b = %d" % b)
    b ^= 5  # 0101
    print("a & b = %d" % b)
