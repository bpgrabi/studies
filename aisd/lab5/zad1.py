def move(sour, dest):
    global count, A, B, C
    count += 1
    dest.append(sour.pop())
    print("rec", count, "\t", A, B, C) #show hanoi after the move


def hanoi(n, sour, dest, buff):
    if n == 1:
        move(sour, dest)
        return
    hanoi(n-1, sour, buff, dest)
    move(sour, dest)
    hanoi(n-1, buff, dest, sour)


b = 0 #bool, needet to while
while b == 0: #security against wrong input eg "fsdgfsdf" instead "7"
    try:
        n = int(input("chose a number of disc"))
        #n = 25 #hardcode is comfortable in task 3
        A = list(range(n, 0, -1)) #create a sorce array with numbered "discs"
        B, C = [], [] #buffor and destination arrays
        print(A, B, C) #show hanoi before start
        count = 0
        hanoi(n, A, C, B) #start
        print("in total, we need", count, "moves") #show how many moves are needed
        b = 1 #ending while
    except ValueError:
        print("it's not a number")
