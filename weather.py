#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# Content：
# 地址：http: //www.runoob.com/python/python-exercise-example.html

# 知识点：
# 地址：
# Notes:

from bs4 import BeautifulSoup
import requests, sys, urllib2

reload(sys)
sys.setdefaultencoding("utf8")
wttr = "http://wttr.in/?format=1"
wttrre = urllib2.Request(wttr)
wttrpon = urllib2.urlopen(wttrre, timeout=60)
wttrapi = wttrpon.read().replace("\n", "")
print(wttrapi)
print("---")
fwttr = "http://wttr.in?0"
fwttrre = urllib2.Request(fwttr)
fwttrpon = urllib2.urlopen(fwttrre, timeout=60)
fwttrapi = fwttrpon.read()
fbs = BeautifulSoup(fwttrapi, "html.parser")
a = (
    str(fbs.body.get_text())
    .replace("\n\n", "\n")
    .replace("\n", "| trim=false size=16 color=#FFFFFF font=Courier New \n")
)
print(a)

# //TODO 改造为Python3 的版本
