#!#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：
# 地址：http: //www.runoob.com/python/python-exercise-example73.html

# 知识点：Python 链表

if __name__ == "__main__":
    ptr1 = [3, 6, 5, 1, 7]
    ptr2 = [5, 1, 0, 4, 9]
    ptr1.sort()
    print(ptr1)

    ptr = ptr1 + ptr2
    print(ptr)

    ptr1.extend(ptr2)
    print(ptr1)

# TODO：ptr3=ptr1.extend(ptr2), 再次赋值为None
