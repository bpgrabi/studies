import zad1, zad2
import random
import time


creasum, printsum, maxsum, minsum, searsum = 0, 0, 0, 0, 0
for co in range(0, 6):
    n = 100 #nuber of roots
    m = 10000 #average number of elements in a single tree
    stime = time.perf_counter_ns()
    arr = zad2.tree(n)
    for j in range(0, m*n): #average m elements per 1 root
        arr.insert((random.randint(0, 100000*n - 1)) / 100000)
    etime = time.perf_counter_ns()
    creat = etime - stime

    stime = time.perf_counter_ns()
    arr.printing()
    etime = time.perf_counter_ns()
    prin = etime - stime

    print("max, min, shearch")
    for i in range(0, n):
        stime = time.perf_counter_ns()
        arr.maximum(i + 0.1)
        etime = time.perf_counter_ns()
        maxsum += etime - stime

    for i in range(0, n):
        stime = time.perf_counter_ns()
        arr.minimum(i + 0.1)
        etime = time.perf_counter_ns()
        minsum += etime - stime

    for i in range(0, n):
        stime = time.perf_counter_ns()
        arr.search(i + 0.78)
        etime = time.perf_counter_ns()
        searsum += etime - stime

    creasum += creat
    printsum += prin
    print(co)

print("creating new trees:", creasum, "ns")
print("printing trees:", printsum, "ns")
print("looking for max:", maxsum, "ns")
print("looking for min:", minsum, "ns")
print("checking existing:", searsum, "ns")
