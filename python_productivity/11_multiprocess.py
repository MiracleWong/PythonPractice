from multiprocessing import Pool,Queue
import psutil
import os
import time

# 逻辑cpu的个数
count = psutil.cpu_count()

# 定义一个队列用于存储进程id
queue = Queue()

def f(x):
    queue.put(os.getpid())
    return x*x

if __name__ == '__main__':

    # 并行计算时间统计
    with Pool(count*2) as p:
        time1 = time.time()
        res = p.map(f, range(1, 101))
        print(f'计算平方的结果是:{res}')
        time2 = time.time()

    print(str(time2 - time1))
    pids = set()
    while not queue.empty():
        pids.add(queue.get())

    print(f'用到的进程id是：{pids}')

    # 串行计算时间统计
    list1 = []

    time1 = time.time()
    for i in range(1, 10001):
        list1.append(f(i))
    time2 = time.time()

    print(str(time2 - time1))