#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http://www.runoob.com/python/python-exercise-example15.html
score = int(input("请输入学习成绩（分数）: \n"))

if score >= 90:
    grade = "A"
elif score >= 60:
    grade = "B"
else:
    grade = "C"


print("%d 属于 %s" % (score, grade))

