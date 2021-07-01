import zad1, zad2
import random
import time


creasum, printsum, maxsum, minsum, searsum = 0, 0, 0, 0, 0
for co in range(0, 6):
    n = 300000
    stime = time.time()
    arr = zad2.tree(n)
    for j in range(0, 100*n): #average 100elements per 1 root
        arr.insert((random.randint(0, 100*n - 1)) / 100)
    etime = time.time()
    creat = etime - stime

    stime = time.time()
    arr.printing()
    etime = time.time()
    prin = etime - stime

    print("max, min, shearch")
    stime = time.time()
    for i in range(0, n):
        arr.maximum(i + 0.1)
    etime = time.time()
    max = etime - stime

    stime = time.time()
    for i in range(0, n):
        arr.minimum(i + 0.1)
    etime = time.time()
    min = etime - stime

    stime = time.time()
    for i in range(0, n):
        arr.search(i + 0.78)
    etime = time.time()
    sear = etime - stime

    creasum += creat
    printsum += prin
    maxsum += max
    minsum += min
    searsum += sear
    print(co)

print("creating new trees:", creasum, "s")
print("printing trees:", printsum, "s")
print("looking for max:", maxsum, "s")
print("looking for min:", minsum, "s")
print("checking existing:", searsum, "s")
