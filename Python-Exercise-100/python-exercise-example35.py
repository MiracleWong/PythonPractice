#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Content：Python实现文本颜色输出
# 地址：http: //www.runoob.com/python/python-exercise-example.html

# 知识点：Python 颜色
# 地址：https://www.cnblogs.com/easypython/p/9084426.html https://www.cnblogs.com/MrHB/p/9080369.html
# Notes:
# 显示方式: 0（默认值）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
# 前景色: 30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
# 背景色: 40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋 红）、46（青色）、47（白色）


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BLACKGREEN = "\033[1;32;40m"
    CYANGRED = "\033[0;31;46m"


print(bcolors.HEADER + "警告的颜色字体?" + bcolors.ENDC)
print(bcolors.OKBLUE + "警告的颜色字体?" + bcolors.ENDC)
print(bcolors.OKGREEN + "警告的颜色字体?" + bcolors.ENDC)
print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)
print(bcolors.FAIL + "警告的颜色字体?" + bcolors.ENDC)
print(bcolors.BOLD + "警告的颜色字体?" + bcolors.ENDC)
print(bcolors.UNDERLINE + "警告的颜色字体?" + bcolors.ENDC)
print(bcolors.BLACKGREEN + "警告的颜色字体?" + bcolors.ENDC)
print(bcolors.CYANGRED + "警告的颜色字体?" + bcolors.ENDC)
