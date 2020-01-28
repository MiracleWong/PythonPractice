#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http://www.runoob.com/python/python-exercise-example10.html

import time, datetime

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

# 暂停一秒
time.sleep(1)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

# 暂停一秒
time.sleep(1)

TIME = datetime.datetime.now()
print(TIME.strftime("%Y-%m-%d %H:%M:%S"))

