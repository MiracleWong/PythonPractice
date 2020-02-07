#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example79.html

if __name__ == "__main__":
    # string_list = ["MiracleWong", "Hello World", "Hello Miracle"]
    string_list = []
    for i in range(3):
        string_list.append(input("int something:"))
    string_list.sort()
    print(string_list)
