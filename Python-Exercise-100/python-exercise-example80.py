#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example80.html

# 知识点：逆向思维

num = int(input("输入猴子的数目:"))


def fn(n):
    if n == num:
        return 4 * x  # 最后剩的桃子的数目
    else:
        return fn(n + 1) * 5 / 4 + 1


x = 1
while 1:
    count = 0
    for i in range(1, num):
        if fn(i) % 4 == 0:
            count = count + 1
    if count == num - 1:
        print("海滩上原来最少有%d个桃子" % int(fn(0)))
        break
    else:
        x = x + 1


# if __name__ == "__main__":
#     i = 0
#     j = 1
#     x = 0
#     while i < 5:
#         x = 4 * j
#         for i in range(0, 5):
#             if x % 4 != 0:
#                 break
#             else:
#                 i += 1
#             x = (x / 4) * 5 + 1
#         j += 1
#     print(int(x))

# TODO Python练习里面其他的作者的解法，其实考虑的还不是很全面，他是考虑的在同样的分法（规则）的情况下，多个猴子（大于5）的时候的桃子的最小个数的值
# TODO 其实我们可以考虑，规则（分桃子的方法）其实是和猴子的数量有关系的：5个猴子，所以分成5份，拿走1份，留下4份，丢掉一个）。如果是六个猴子的话，应该为：6个猴子，所以分成6份，拿走1份，留下5份，丢掉1个（这个值也是可以改变的）
# TODO 其实还可以将规则（分桃子的方法），份数和猴子的数量解离开，没有关系，让用户输入值，同时输入可以丢掉的桃子的数量
# TODO丢掉的桃子的数量应该小于份数
