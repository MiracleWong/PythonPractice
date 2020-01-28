#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：正整数分解质因数
# 地址：http: //www.runoob.com/python/python-exercise-example14.html

# 知识点：Python如何判断一个质数
# 地址：https://www.runoob.com/python3/python3-prime-number.html
# Notes:


def reduceNum(n):
    print("{} = ".format(n), end="")
    if not isinstance(n, int) or n <= 0:
        print("请输入一个正确的数字 !")
        exit(0)
    elif n in [1]:
        print("{}".format(n))
    while n not in [1]:  # 循环保证递归
        for index in range(2, n + 1):
            if n % index == 0:
                n = int(n / index)  # n 等于 n/index
                if n == 1:
                    print(index)
                else:  # index 一定是素数
                    print("{} * ".format(index), end="")
                break


if __name__ == "__main__":
    reduceNum(10)
    reduceNum(100)
    reduceNum(1000)
    reduceNum(10000)
    reduceNum(9)
    reduceNum(90)
    reduceNum(900)
    reduceNum(9000)


# // TODO print 在Python2 和 Python3 版本中的异同
# // TODO n = int(n / index)
