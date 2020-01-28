#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：水仙花数
# 地址：http://www.runoob.com/python/python-exercise-example13.html

# 知识点：range
# 地址：https://www.runoob.com/python/python-func-range.html
# Notes:
# range(start, stop[, step])
# range 左闭右开 [start, stop), 默认start 为 0， 默认step 为 1
for num in range(100, 1000):
    i = int(num / 100)  # 百位
    j = int(num / 10 % 10)  # 十位
    k = num % 10  # 个位
    # print("{} - {} - {}".format(i, j, k))
    if num == i ** 3 + j ** 3 + k ** 3:
        print(num)

// TODO range