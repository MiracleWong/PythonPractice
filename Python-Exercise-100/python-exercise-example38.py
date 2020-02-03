#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：主对角线之和
# 地址：http: //www.runoob.com/python/python-exercise-example38.html

# 知识点：二维数组
# 地址：
# Notes:

if __name__ == "__main__":
    a = []
    # for i in range(3):
    #     a.append([])
    #     for j in range(3):
    #         a[i].append(float(input("input num:\n")))
    # a = [[1, 2, 3], [4, 5, 6], [0, 0, 0]]
    # a[0] = [1, 2, 3]
    # a[1] = [4, 5, 6]
    # a[2] = [0, 0, 0]
    a[0][0] = 1
    a[0][1] = 2
    a[0][2] = 3
    a[1][0] = 4
    a[1][1] = 5
    a[1][2] = 6
    a[2][0] = 7
    a[2][1] = 8
    a[2][2] = 9

    sum = 0.0
    for i in range(3):
        sum += a[i][i]
    print(sum)
