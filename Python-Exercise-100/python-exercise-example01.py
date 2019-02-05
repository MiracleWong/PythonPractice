#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 地址：http://www.runoob.com/python/python-exercise-example1.html

# 示例程序
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if(i != k) and (i != j) and (j != k):
#                 print i, j, k


# 知识点：列表生成式
# 地址：https: // www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431779637539089fd627094a43a8a7c77e6102e3a811000

def create_three_digits(number_start=1, number_end=4):
    return [str(i) + ' ' + str(j) + ' ' + str(k) for i in range(number_start, number_end + 1) for j in
            range(number_start, number_end + 1) for k in
            range(number_start, number_end + 1) if (i != j) and (i != k) and (j != k)]


if __name__ == "__main__":
    print(create_three_digits(1, 4))
