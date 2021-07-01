def move(sour, dest):
    global count, A, B, C
    count += 1
    if len(dest) > 0 and len(sour) > 0:
        if int(sour[-1]) < int(dest[-1]):
            dest.append(sour.pop())
        else:
            sour.append(dest.pop())
    elif len(sour) > 0:
        dest.append(sour.pop())
    elif len(dest) > 0:
        sour.append(dest.pop())
    print("ite", count, "\t", A, B, C)


def hanoi(n, sour, dest, buff):
    global count
    if n % 2 == 1:
        while len(sour) > 0 or len(buff) > 0:
            if count % 3 == 0:
                move(sour, dest)
            elif count % 3 == 1:
                move(sour, buff)
            elif count % 3 == 2:
                move(buff, dest)
    else:
        while len(sour) > 0 or len(buff) > 0:
            if count % 3 == 1:
                move(sour, dest)
            elif count % 3 == 0:
                move(sour, buff)
            elif count % 3 == 2:
                move(buff, dest)


if __name__ == "__main__":
    b = 0
    while b == 0:
        try:
            n = int(input("chose a number of disc"))
            #n = 25
            A = list(range(n, 0, -1))
            B, C = [], []
            print(A, B, C)
            count = 0
            hanoi(n, A, C, B)
            print("in total needed", count, "moves")
            b = 1
        except ValueError:
            print("it's not a number")
