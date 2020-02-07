#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example86.html
if __name__ == "__main__":
    a = "acegikm"
    b = "bdfhjlnpq"
    e = "Hello World"
    delimiter = ","
    # 连接字符串
    c = a + b
    d = a + "-" + b
    print(c)
    print(d)
    print(delimiter.join([a, b, e]))
