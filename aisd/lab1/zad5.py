import random


def table(space):
    for ij in range(0, 3):
        print("_____________")
        print("|", space[3*ij], "|", space[3*ij + 1], "|",  space[3*ij + 2], "|")
    print("_____________")


def move(counter, tab, computer):
    print("if u want move, choose number from range (1, 9), which is free")
    co = 1
    pos = 100
    if counter % 2 == 0:
        while co != 0:
            try:
                if computer == 1:
                    pos = random.randint(1, 9)
                if computer == 0:
                    pos = int(input("Move x, choose the place"))
                if 0 < pos < 10 and tab[pos - 1] == " ":
                    tab[pos - 1] = "x"
                    co = 0
                else:
                    print("wrong move, pls choose from range (1, 9), which isnt o")
            except ValueError:
                print("wrong move, pls choose from range (1, 9), which isnt o")
    else:
        while co != 0:
            try:
                pos = int(input("Move o, choose the place"))
                if 0 < pos < 10 and tab[pos - 1] == " ":
                    tab[pos - 1] = "o"
                    co = 0
                else:
                    print("wrong move, pls choose from range (1, 9), which isnt x")
            except ValueError:
                print("wrong move, pls choose from range (1, 9), which isnt x")
    return tab


def check(tab, co):
    for j in range(0, 3):
        if ((tab[j] == tab[j + 1] and tab[j] == tab[j + 2] and tab[j] != tab[9])
                or (tab[j] == tab[j + 3] and tab[j] == tab[j + 6] and tab[j] != tab[9])
                or (tab[0] == tab[4] and tab[0] == tab[8] and tab[0] != tab[9])
                or (tab[2] == tab[4] and tab[2] == tab[6] and tab[2] != tab[9])):
            if co % 2 == 0:
                print("x win")
            else:
                print("o win")
            return 10
        else:
            return 0


def ejaj():
    while True:
        ai = input("do u want play with 'ai'? 'ai' will be 'x' Y/N")
        try:
            if ai == "Y" or ai == "y":
                return 1
            if ai == "N" or ai == "n":
                return 0
        except ValueError:
            print("use T or F")


paper = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
comp = ejaj()
i = 1
while i < 10:
    table(paper)
    paper = move(i, paper, comp)
    i = i + 1 + check(paper, i)
table(paper)
