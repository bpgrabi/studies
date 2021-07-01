import time
import array as arr
stime = time.time()
L = arr.array('f', [1]*48)
L[1] = 2
for i in range(2, 48, 1):
    L[i] = ((L[i-1] + L[i-2])/(L[i-1] - L[i-2]))
    print(i, ": ", L[i])
average = sum(L)/48
print("average = ", average)
count = 0
for i in range(0, 48):
    for j in range(i+1, 48):
        if i != j:
            if L[i] > L[j]:
                a, b = L[i], L[j]
                L[i], L[j] = b, a
            if L[i] == L[j]:
                print(L[i], " repetition")
                count = 1
                break
median = (L[23] + L[24])/2
print("median = ", median)
if count == 0:
    print("no repetitions")
etime = time.time() - stime
print("time: ", etime)
print("w tym przypadku czas wykonywania kodu nie schodzi (przynajmniej u mnie) ponieżej 0.00099s,\n"
      "a w przypadku kodu z zadania 1 zdarzało się, że timer wyświetlał 0.0,\n"
      "ale tylko wtedy kiedy używałem komendy sort do listy; do tablicy musiałem sam napisać \n"
      "sortowanie, które zapewne nie jest tak wydajne jakby mogło być i bardzo obciąża cały proces \n"
      "Po zmienieniu sortowania, na identyczne w obu przypadkach, czasy wychodzą bardzo zbliżone")
