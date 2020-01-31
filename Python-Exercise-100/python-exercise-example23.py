#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：
# 地址：http: //www.runoob.com/python/python-exercise-example.html

# 知识点：
# 地址：
# Notes:

from sys import stdout

for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(" ")
    for k in range(2 * i + 1):
        stdout.write("*")
    print()
for i in range(3):
    for j in range(i + 1):
        stdout.write(" ")
    for k in range(2 * (2 - i) + 1):
        stdout.write("*")
    print()

