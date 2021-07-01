import part1
import time

stime = time.time()

size = 1000
with open("./packages/packages" + str(size) + ".txt") as txt:
    lines = [line for line in txt]

items = []
for i in range(2, len(lines)):
    data = lines[i].split(",")
    items.append(part1.item(int(data[1]), int(data[2]), int(data[3])))

part1.sort(items)

back = part1.backpack(size)

for i in range(0, len(items)):
    back.add(items[i])

back.print()

etime = time.time()
time = etime - stime
print(time)
