#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example93.html

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    for i in range(100000):
        print(i, end=" ")
    end = time.perf_counter()
    print()
    print("different is %6.3f" % (end - start))

