#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example85.html


def func(num):
    j = 1
    sum = 9
    m = 9
    flag = True
    while flag:
        if sum % num == 0:
            print(sum)
            flag = False
        else:
            m *= 10
            sum += m
            j += 1
    print("%d 个 9 可以被 %d 整除 : %d" % (j, num, sum))
    r = sum / num
    print("%d / %d = %d" % (sum, num, r))


# 给出一个奇数需要多少个99 才可以除尽它
if __name__ == "__main__":
    num = 21
    # num = int(input("请输入一个正奇数："))
    if num > 0 and num % 2 == 1:
        func(num)
    else:
        print("输入错误")

