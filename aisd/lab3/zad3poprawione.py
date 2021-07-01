import random
import math


def integral(function, start, end, sample):
    hit = 0
    a = int(start)
    b = int(end)
    c, d = 0, 0

    for i in range(a*10, b*10 + 1):
        x = i * 0.1
        func = math.cos(x) #nie miałem pojęcia jak mogę zmienić funkcję, którą chcę całkować więc ją wpisałem na sztywno
        if c > func:
            c = func
        if d < func:
            d = func
    print(c, " ", d)
    for i in range(0, sample):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        func = math.cos(x)
        fx = func
        if abs(y) < abs(fx):
            if y > 0:
                hit += 1
            if y < 0:
                hit -= 1

    print((b - a) * (d - c))
    print(hit, " ", sample)
    inte = hit / sample * (b - a) * (d - c)
    print("integral of sin(x) from 0 to 2 is: ", inte, " accuracy: ", sample, "samples")


integral("sin", 0, 2, 100000) #nie miałem pomysłu jak mogę zmienić badaną funkcję po przez argument do funkcji całkowania
integral("sin", 0, 2, 100)

print("prawidłowy wynik dla sin(x) to około 1.41 więc jak widać, różnica jest, zwłaszcza przy kilku próbach")
