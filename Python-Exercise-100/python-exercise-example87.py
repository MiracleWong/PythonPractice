#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：结构体
# 地址：http: //www.runoob.com/python/python-exercise-example87.html

if __name__ == "__main__":

    class student:
        x = 0
        c = 0

    def f(stu):
        stu.x = 20
        stu.c = "c"

    a = student()
    a.x = 3
    a.c = "a"
    f(a)
    print(a.x, a.c)

