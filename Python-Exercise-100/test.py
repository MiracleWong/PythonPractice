#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：回文数
# 地址：http: //www.runoob.com/python/python-exercise-example30.html

import re


def find_string(str_in, pat):
    return re.findall(pat, str_in, re.I)


if __name__ == "__main__":
    print(find_string("hello\nworld\n", "wor"))
    print(find_string("hello\nworld\n", "l*d"))
    print(find_string("hello\nworld\n", "o."))
