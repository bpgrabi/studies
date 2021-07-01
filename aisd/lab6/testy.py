import zad1, zad2
import random
import time


creasum, printsum, maxsum, minsum, searsum = 0, 0, 0, 0, 0
for co in range(0, 6):
    n = 100 #number of roots
    m = 100 #number of elemets in 1 tree
    stime = time.perf_counter_ns()
    arr = zad2.tree(n)
    for j in range(0, n):
        for i in range(0, m):
            arr.insert((j*m + i) / m)
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
