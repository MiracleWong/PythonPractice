#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example98.html
if __name__ == "__main__":
    fp = open("test.txt", "w")
    string = input("please input a string:\n")
    string = string.upper()
    fp.write(string)
    fp = open("test.txt", "r")
    print(fp.read())
    fp.close()
