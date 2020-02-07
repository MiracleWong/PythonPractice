#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example99.html
if __name__ == "__main__":
    import string

    fp = open("test1.txt")
    a = fp.read()
    fp.close()

    fp = open("test2.txt")
    b = fp.read()
    fp.close()

    fp = open("test3.txt", "w")
    l = list(a + b)
    l.sort()
    s = ""
    s = s.join(l)
    fp.write(s)
    fp.close()
