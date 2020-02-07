#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http: //www.runoob.com/python/python-exercise-example78.html
# if __name__ == "__main__":
#     person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
#     m = "li"
#     for key in person.keys():
#         if person[m] < person[key]:
#             m = key

#     print("%s,%d" % (m, person[m]))

import operator

if __name__ == "__main__":
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
    print(max(person.items(), key=operator.itemgetter(1))[0])
    print(max(person.values()))

# TODO operator的包的学习
# TODO operator的源码学习
# TODO Python2 和 Python3 版本中dict 的区别
# TODO Python2 和 Python3 版本中的各个区别汇总

