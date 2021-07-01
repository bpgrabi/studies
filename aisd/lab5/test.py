import time

#if u want only check times for both algoryth run this code
stime = time.time()
import zad1
etime1 = time.time() - stime
print(etime1)
stime = time.time()
import zad2
etime2 = time.time() - stime
print(etime2)

print("recurency total time: ", etime1, "\niteration total time: ", etime2)
