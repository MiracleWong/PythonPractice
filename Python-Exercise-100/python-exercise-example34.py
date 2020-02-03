#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：函数调用——无聊
# 地址：http: //www.runoob.com/python/python-exercise-example.html


def hello_world():
    print("hello world")


def three_hellos():
    for i in range(3):
        hello_world()


if __name__ == "__main__":
    three_hellos()
