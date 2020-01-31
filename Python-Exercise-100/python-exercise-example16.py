#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http://www.runoob.com/python/python-exercise-example16.html

import time, datetime


def main():
    print(datetime.datetime.today().strftime("%Y-%m-%d"))

    birthDate = datetime.date(1991, 1, 3)

    print(birthDate.strftime("%d/%m/%Y"))

    # 日期算术运算
    birthNextDay = birthDate + datetime.timedelta(days=1)

    print(birthNextDay.strftime("%d/%m/%Y"))

    # 日期替换
    birthDate = birthDate.replace(year=birthDate.year + 1)

    print(birthDate.strftime("%d/%m/%Y"))


if __name__ == "__main__":
    main()
