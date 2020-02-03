#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：分割列表
# 地址：http: //www.runoob.com/python/python-exercise-example33.html

# 知识点：分割list， join，列表推导式
# 地址：
# Notes

nums = [1, 2, 3, 4, 5, 6]

string_nums = ",".join(str(i) for i in nums)
print(string_nums)
