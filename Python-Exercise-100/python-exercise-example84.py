#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example84.html

delimiter = ","
mylist1 = ["Brazil", "Russia", "India", "China"]
mylist2 = ["Brazil", "Russia", "India", "China"]

print(mylist1 + mylist2)

print(delimiter.join(mylist1).join(mylist2))
