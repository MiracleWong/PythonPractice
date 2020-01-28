#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http://www.runoob.com/python/python-exercise-example9.html
import time

Dictory = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
for key, value in dict.items(Dictory):
    print(key, value)
    time.sleep(1)  # 暂停 1 秒
