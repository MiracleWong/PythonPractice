#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example22.html

# for i in range(ord("x"), ord("z") + 1):
#     for j in range(ord("x"), ord("z") + 1):
#         if i != j:
#             for k in range(ord('x'), ord('z') + 1):
#                 if (i != k) and (j != k):
#                     print(k)
n = ["a", "b", "c"]
m = []
for i in range(3):
    if n[i] != "a" and n[i] != "c":
        m.insert(i, "x")
    elif n[i] != "c":
        m.insert(i, "z")
    else:
        m.insert(i, "y")

print("a--%s, b--%s, c--%s" % (m[0], m[1], m[2]))

