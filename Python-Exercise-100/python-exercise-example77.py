#!#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：无聊：循环输出列表
# 地址：http: //www.runoob.com/python/python-exercise-example77.html

# 知识点：Python 链表

if __name__ == "__main__":
    ptr = ["1", "2", "3", "4", "5"]
    for i in range(len(ptr)):
        print(ptr[i], end="")
    print()
    print(ptr)
