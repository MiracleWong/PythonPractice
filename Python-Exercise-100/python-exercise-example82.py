#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example82.html

if __name__ == "__main__":
    n = 0
    p = input("input a octal number:\n")
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord("0")
    print(n)
    print(ord("a"))
    print(ord("0"))
