#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example62.html
sStr1 = "abcdefg"
sStr2 = "cde"
print(type(sStr1.find(sStr2)))
print(sStr1[sStr1.find(sStr2) : sStr1.find(sStr2) + len(sStr2)])

