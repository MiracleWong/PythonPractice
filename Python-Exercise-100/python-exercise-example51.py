#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：按位与
# 地址：http: //www.runoob.com/python/python-exercise-example51.html

# 知识点：按位与
# 地址：
# Notes:
# 0&0=0; 0&1=0; 1&0=0; 1&1=1。
# 0x77 是16进制
# 0123 是8进制
# 123  是十进制
# 01011010 是二进制
if __name__ == "__main__":
    a = 0x77  # 01110111 十进制结果为119
    b = a & 3  # 0011
    print("a & b = %d" % b)
    b &= 5  # 0101
    print("a & b = %d" % b)

