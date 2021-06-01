#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime

import psutil

# CPU的信息
print(psutil.cpu_times())
print(psutil.cpu_times().user)

print(psutil.cpu_count())

print(psutil.cpu_count(logical=False))

# 内存的信息
mem = psutil.virtual_memory()

print(mem.total/1024/1024, mem.used/1024/1024)
print(mem.total, mem.used)


# 磁盘的信息
print(psutil.disk_partitions())
print(psutil.disk_usage("C:\\"))
print(psutil.disk_usage("D:\\"))
print(psutil.disk_io_counters())

print(psutil.disk_io_counters(perdisk=True))

# 网络信息
print(psutil.net_io_counters())
print(psutil.users())
print(psutil.boot_time())
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))


# 进程信息
print(psutil.pids())
p = psutil.Process(8908)
print(p.name())
print(p.cwd())
print(p.status())
print(p.create_time())
print(datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S"))