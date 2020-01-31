#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http://www.runoob.com/python/python-exercise-example17.html

import string

s = input("请输入一个字符串: \n")
letters = 0
space = 0
digit = 0
others = 0

i = 0

while i < len(s):
    c = s[i]
    i += 1
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1

print(
    "char = {} , space = {} , digit = {} , others = {}".format(
        letters, space, digit, others
    )
)

