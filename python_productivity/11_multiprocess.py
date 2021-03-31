from multiprocessing import Pool,Queue
import psutil
import os

# 逻辑cpu的个数
count = psutil.cpu_count()

# 用于存储进程值
queue = Queue()

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(count*2) as p:
        res = p.map(f, range(1, 101))
        print(f'计算平方的结果是:{res}')