#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：猴子吃桃
# 地址：http: //www.runoob.com/python/python-exercise-example21.html

# 知识点：逆向思维
peach_10 = 1
peach_day = peach_10
peach_total = 0
for day in range(9, 0, -1):
    peach_tmp = (peach_day + 1) * 2
    peach_day = peach_tmp

peach_total = peach_tmp
print("桃子的总数为：{}".format(peach_total))

