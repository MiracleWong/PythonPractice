#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：随机数
# 地址：http: //www.runoob.com/python/python-exercise-example50.html

# 知识点：random模块
# 地址：https://docs.python.org/3/library/random.html
# Notes:
# random.randint(a,b) 返回(a,b) 内的一个随机数
# random.random() 返回[0,1) 内的一个随机浮点数

import random

print(random.randint(34, 100))

# 生成第一个随机数
print("random() : ", random.random() * 100)

# 生成第二个随机数
print("random() : ", random.random() * 100)
