#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：矩阵的相加
# 地址：http: //www.runoob.com/python/python-exercise-example44.html

X = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]

Y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]

# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(len(X))
# for n in range(len(X)):
#     for m in range(len(X[0])):
#         result[n][m] = X[n][m] + Y[n][m]

# for r in result:
#     print(r)


import numpy as np

x = np.array(X)
y = np.array(Y)
result = x + y
print(result)
