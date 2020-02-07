#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example92.html

if __name__ == "__main__":
    import time

    start = time.time()
    for i in range(300):
        print(i, end=" ")
    end = time.time()
    print()

    print(end - start)

