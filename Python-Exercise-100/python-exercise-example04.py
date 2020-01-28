#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http://www.runoob.com/python/python-exercise-example4.html
import sys

year = int(input("year:\n"))
month = int(input("month:\n"))
day = int(input("day:\n"))
print(sys.version)

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print("input error")

sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1

print("{}-{}-{} is the {}th day ".format(year, month, day, sum))

# 可以通过 date +%j  命令实现
