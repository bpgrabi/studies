import time

stime = time.time()
L = [1, 2]

for i in range(2, 48):
    L.append((L[i-1] + L[i-2])/(L[i-1] - L[i-2]))
    print(i, ": ", L[i])
average = sum(L)/48
print("average = ", average)
count = 0
for i in range(2, 48):
    for j in range(i+1, 47):
        if i != j:
            if L[i] > L[j]:
                a, b = L[i], L[j]
                L[i], L[j] = b, a
            if L[i] == L[j]:
                print(L[i], " repetition")
                count = 1
                break
median = (L[23]+L[24])/2
print("median = ", median)
if count == 0:
    print("no repetitions")
etime = time.time() - stime
print("time: ", etime)
