#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys

if (3, 5) > sys.version_info > (2, 7):
    print("Python 2")
elif sys.version_info >= (3, 5):
    print("Python 3")


# ipython 的 history 必须是在当时打开的ipython shell 里面才是有效的。
# 退出后，再进去，就是么有任何历史记录的
