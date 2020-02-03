#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：质数
# 地址：http: //www.runoob.com/python/python-exercise-example36.html

# 知识点：质数求法
# 地址：
# Notes:


def prime(lower, upper):
    for num in range(lower, upper + 1):
        # 素数大于 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


if __name__ == "__main__":
    prime(1, 100)
