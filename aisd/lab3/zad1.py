import os
import time


stime = time.time()

for file in os.listdir("./zadanie1"):
    try:
        os.mkdir("./zadanie1/" + file[0])
    except FileExistsError:
        pass
    os.rename("./zadanie1/" + file, "./zadanie1/" + file[0] + "/" + file)

etime = time.time()
print(etime - stime)

### wraz z zadaniem przesyłam nieposortowany folder "zadanie1"
