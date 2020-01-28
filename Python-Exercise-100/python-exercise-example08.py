#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 地址：http://www.runoob.com/python/python-exercise-example8.html
import json

# ## 示例代码1
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("{} * {} = {}".format(j, i, i * j), end="\t")
#     print()

# ## 示例代码2
# print(
#     "\n".join(
#         [
#             " ".join(["%s*%s=%-2s " % (j, i, j * i) for j in range(1, i + 1)])
#             for i in range(1, 10)
#         ]
#     )
# )
print(
    "\n".join(
        [
            " ".join(
                [
                    "%s*%s=%s " % (j, i, j * i)
                    if j == 1
                    else "%s*%s=%-2s " % (j, i, j * i)
                    for j in range(1, i + 1)
                ]
            )
            for i in range(1, 10)
        ]
    )
)


# 可参考地址：https://www.cnblogs.com/wangyi0419/p/11229460.html
