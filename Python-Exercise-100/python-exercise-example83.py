#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example83.html

# if __name__ == "__main__":
#     sum = 4
#     s = 4
#     for j in range(2, 9):
#         print(sum)
#         if j <= 2:
#             s *= 7
#         else:
#             s *= 8
#         sum += s
#     print("sum = %d" % sum)


def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 7
    else:
        return f(n - 1) * 8


l = []
# 算出每位数有多少奇数
for i in range(1, 9):
    l.append(f(i - 1) * 4)
print(l)
# 输出一共有多少个奇数
print(sum(l))

# TODO 看了看题目的要求，也就是说每个数字都是可以重复使用多次的
