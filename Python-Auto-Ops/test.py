#!/usr/bin/python
# -*- coding: UTF-8 -*-

import psutil

mem = psutil.virtual_memory()

print(psutil.cpu_times())

print(mem.total/1024/1024, mem.used/1024/1024)
print(mem.total, mem.used)