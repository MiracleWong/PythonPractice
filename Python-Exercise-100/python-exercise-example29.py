#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：逆序输出
# 地址：http: //www.runoob.com/python/python-exercise-example29.html


# num = list(input("输入一个最多5位的数字:"))
num = list("12345")
print("num的位数为：{}".format(len(num)))
num.reverse()
print("逆序输出为:", end=" ")
for i in range(len(num)):
    print(num[i], end="")
