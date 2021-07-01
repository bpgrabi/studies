import random
import time


def insertionsort(A):
    for i in range(1, len(A)):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = x


def merge(A, a, c, b):
    n1 = c - a + 1
    n2 = b - c
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = A[a + i]
    for i in range(0, n2):
        R[i] = A[c + 1 + i]
    i, j, k = 0, 0, a
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1


def mergesort(A, a, b):
    if a < b:
        c = int((a + b) / 2)
        mergesort(A, a, c)
        mergesort(A, c + 1, b)
        merge(A, a, c, b)


leng = 60000000
tab = leng*[0]
arr = leng*[0]
stime = time.time()
for t in range(0, 150):
    for i in range(0, leng):
        tab[i] = random.randint(100000, 999999)
    #print(tab)
    subtime = time.time()
    mergesort(arr, 0, leng - 1)
    #print(tab)
    print(time.time() - subtime)
end1 = time.time() - stime
print(end1)


print("_______________________")
stime = time.time()
for t in range(0, 150):
    for i in range(0, leng):
        arr[i] = random.randint(100000, 999999)
    #print(arr)
    subtime = time.time()
    insertionsort(tab)
    #print(arr)
    print(time.time() - subtime)
end2 = time.time() - stime
print(end2)

print("\nFirst sort:", end1, "\nSecond sort:", end2)
