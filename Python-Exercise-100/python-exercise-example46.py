#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：平方和
# 地址：http: //www.runoob.com/python/python-exercise-example46.html


def square(n):
    return n * n


if __name__ == "__main__":
    num = 0
    flag = 1
    while flag:
        n = int(input("please input a num: \n"))
        num = square(n)
        if num > 50:
            print(num)
            flag = 1
        else:
            flag = 0
