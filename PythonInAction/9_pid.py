#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import string


def isNum(s):
    for i in s:
        if i in string.digits:
            continue
        else:
            return False
    return True


for pid in os.listdir('/proc'):
    if pid.isdigit():
        # if isNum(pid):
        print(pid)
