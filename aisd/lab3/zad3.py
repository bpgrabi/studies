import random
import math


a, b = 0, 2
c, d = 0, 1
sample = 100000
hit = 0

for i in range(0, sample):
    x = random.uniform(a, b)
    y = random.uniform(c, d)
    if abs(y) < abs(math.sin(x)):
        if y > 0:
            hit += 1
        if y < 0:
            hit -= 1

integral = hit / sample * (b - a) * (d - c)
print("integral of sin(x) from 0 to 2 is: ", integral, " accuracy: ", sample, "samples")

sample = 100
hit = 0

for i in range(0, sample):
    x = random.uniform(a, b)
    y = random.uniform(c, d)
    if abs(y) < abs(math.sin(x)):
        if y > 0:
            hit += 1
        if y < 0:
            hit -= 1

integral = hit / sample * (b - a) * (d - c)
print("integral of sin(x) from 0 to 2 is: ", integral, " accuracy: ", sample, " samples")
