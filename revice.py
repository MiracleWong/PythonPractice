#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pathlib

file_name = "137.txt"

# 取得脚本所在目录
current_path = pathlib.PurePath(__file__).parent
# 和脚本同目录下的文件绝对路径
file = current_path.joinpath(file_name)

if __name__ == '__main__':
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        print("\n".join(content.split("\n")[::-1]))
