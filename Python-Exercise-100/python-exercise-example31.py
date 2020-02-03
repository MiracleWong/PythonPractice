#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：re
# 地址：http: //www.runoob.com/python/python-exercise-example31.html

# 知识点：re模块
# 地址：https://www.runoob.com/python/python-reg-expressions.html
# Notes: 

import re


def judge(list, first):
    li = []
    first = first.upper()
    for a in list:
        if re.match(first, a):
            # print(a)
            li.append(a)
    if len(li) == 1:
        print(li[0])
    else:
        second = input("请输入第二个字母：")
        # second = "a"
        for b in li:
            if re.match(first + second, b):
                print(b)


list_week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
first = input("请输入第一个字母：")
judge(list_week, first)
