#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：递归反序打印字符串
# 地址：http: //www.runoob.com/python/python-exercise-example27.html


# def output(s, l):
#     if l == 0:
#         return
#     print(s[l - 1], end="")
#     s.pop()
#     output(s, l - 1)


# if __name__ == "__main__":
#     s = input("输入一个字符串: \n")
#     l = len(s)
#     output(s, l)

S = input("Input a string:")
# # TestCase
# S = "Hello World"
L = list(S)
L.reverse()
for i in range(len(L)):
    print(L[i], end="")
